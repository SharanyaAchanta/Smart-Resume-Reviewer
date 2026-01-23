# components/comparison_view.py
import streamlit as st
import pandas as pd


def show_batch_summary(summary: dict):
    """
    Displays summary statistics for batch analysis.

    Args:
        summary: Dictionary containing batch analysis summary statistics
    """
    st.markdown("### 📊 Batch Analysis Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Files", summary["total_files"])
        st.metric("✅ Successful", summary["successful"], delta=None)

    with col2:
        st.metric("Average Score", f"{summary['average_score']:.1f}/100")
        st.metric("❌ Failed", summary["failed"], delta=None)

    with col3:
        st.metric("Highest Score", f"{summary['highest_score']}/100")
        st.metric("📈 Avg Keyword Match", f"{summary['average_keyword_match']:.1f}%")

    with col4:
        st.metric("Lowest Score", f"{summary['lowest_score']}/100")
        if summary["best_resume"]:
            st.success(f"🏆 Best: {summary['best_resume'][:20]}...")


def show_comparison_table(results: list, sort_by: str = "score"):
    """
    Displays batch analysis results in a sortable table.

    Args:
        results: List of analysis result dictionaries
        sort_by: Column to sort by (default: "score")
    """
    st.markdown("### 📋 Resume Comparison Table")

    if not results:
        st.warning("No results to display.")
        return

    # Filter successful results
    successful = [r for r in results if r["status"] == "success"]
    failed = [r for r in results if r["status"] == "error"]

    if not successful:
        st.error("All resume analyses failed. Please check your files and try again.")
        return

    # Create DataFrame for successful results
    df = pd.DataFrame([
        {
            "Filename": r["filename"],
            "Score": r["score"],
            "Keyword Match (%)": r["keyword_match"],
            "Predicted Role": r["predicted_role"],
            "Word Count": r["word_count"],
            "Issues Found": len(r["suggestions"])
        }
        for r in successful
    ])

    # Sort options
    col1, col2 = st.columns([3, 1])
    with col1:
        sort_column = st.selectbox(
            "Sort by:",
            options=["Score", "Keyword Match (%)", "Word Count", "Issues Found"],
            index=0,
            key="batch_sort_column"
        )
    with col2:
        sort_order = st.radio(
            "Order:",
            options=["Descending", "Ascending"],
            index=0,
            horizontal=True,
            key="batch_sort_order"
        )

    # Sort DataFrame
    ascending = (sort_order == "Ascending")
    df_sorted = df.sort_values(by=sort_column, ascending=ascending)

    # Display table with color coding
    st.dataframe(
        df_sorted.style.background_gradient(subset=["Score"], cmap="RdYlGn", vmin=0, vmax=100)
                      .background_gradient(subset=["Keyword Match (%)"], cmap="Blues", vmin=0, vmax=100),
        use_container_width=True,
        height=min(400, 50 + len(df_sorted) * 35)
    )

    # Show failed files if any
    if failed:
        with st.expander(f"⚠️ {len(failed)} Failed Analysis", expanded=False):
            for fail in failed:
                st.error(f"**{fail['filename']}**: {fail.get('error', 'Unknown error')}")


def show_batch_charts(results: list):
    """
    Displays visual charts for batch analysis results.

    Args:
        results: List of analysis result dictionaries
    """
    st.markdown("### 📈 Visual Analysis")

    successful = [r for r in results if r["status"] == "success"]
    if not successful:
        st.warning("No successful results to visualize.")
        return

    # Create DataFrame
    df = pd.DataFrame([
        {
            "Filename": r["filename"],
            "Score": r["score"],
            "Keyword Match": r["keyword_match"]
        }
        for r in successful
    ])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Score Distribution")
        st.bar_chart(df.set_index("Filename")["Score"])

    with col2:
        st.markdown("#### Keyword Match Distribution")
        st.bar_chart(df.set_index("Filename")["Keyword Match"])


def show_detailed_results(results: list):
    """
    Displays detailed analysis results for each resume with expandable sections.

    Args:
        results: List of analysis result dictionaries
    """
    st.markdown("### 🔍 Detailed Results")

    successful = [r for r in results if r["status"] == "success"]
    if not successful:
        st.warning("No successful results to display.")
        return

    for idx, result in enumerate(successful, 1):
        with st.expander(f"📄 {idx}. {result['filename']} - Score: {result['score']}/100", expanded=False):
            # Metrics row
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Resume Score", f"{result['score']}/100")
            with col2:
                st.metric("Keyword Match", f"{result['keyword_match']}%")
            with col3:
                st.metric("Predicted Role", result['predicted_role'])

            # Suggestions
            if result["suggestions"]:
                st.markdown("**💡 Improvement Suggestions:**")
                for suggestion in result["suggestions"]:
                    st.warning(suggestion)
            else:
                st.success("✅ No major issues found!")

            # Resume preview (first 500 characters)
            with st.expander("👁️ Resume Preview", expanded=False):
                preview_text = result["plain_text"][:500]
                st.text_area(
                    "Resume Content Preview",
                    value=preview_text + "...",
                    height=200,
                    disabled=True,
                    key=f"preview_{idx}"
                )


def show_comparison_view(results: list, summary: dict):
    """
    Main function to display complete batch analysis comparison view.

    Args:
        results: List of analysis result dictionaries
        summary: Dictionary containing batch summary statistics
    """
    if not results:
        st.info("No results to display.")
        return

    # Summary
    show_batch_summary(summary)

    st.markdown("---")

    # Comparison table
    show_comparison_table(results)

    st.markdown("---")

    # Charts
    show_batch_charts(results)

    st.markdown("---")

    # Detailed results
    show_detailed_results(results)
