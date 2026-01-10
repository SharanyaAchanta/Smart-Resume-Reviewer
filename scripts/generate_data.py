import json
import random
import csv
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

def load_job_roles():
    try:
        with open("utils/job_roles.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: utils/job_roles.json not found.")
        return {}

def generate_synthetic_data(num_samples_per_role=100):
    job_roles = load_job_roles()
    data = []

    print("Generating extended synthetic data...")
    
    for category, roles in job_roles.items():
        for role, details in roles.items():
            required_skills = details.get("required_skills", [])
            description = details.get("description", "")
            
            # Generate multiple variations for each role
            for _ in range(num_samples_per_role):
                # 1. High Quality / Standard Resume Summary
                selected_skills = random.sample(required_skills, k=min(len(required_skills), random.randint(3, len(required_skills))))
                random.shuffle(selected_skills)
                
                templates = [
                    f"Experienced {role} with a strong background in {', '.join(selected_skills)}.",
                    f"Seeking a position as a {role}. Proficient in {', '.join(selected_skills)}.",
                    f"Skilled in {', '.join(selected_skills)}. {description}.",
                    f"History of working as a {role} handling {description}.",
                    f"Passionate about {category} and {role} roles. core competencies: {', '.join(selected_skills)}.",
                    f"As a {role}, I have deployed systems using {selected_skills[0]} and {selected_skills[1]}.",
                    f"Resume: {role}. Skills: {', '.join(selected_skills)}."
                ]
                
                text = random.choice(templates)
                
                # Add jargon
                if random.random() > 0.7:
                    text += " Proven track record of success in agile environments."
                
                data.append([text, role])

            # 2. "Bad" / Short / Noisy Examples (still labeled as the role, but harder)
            # This teaches the model to pick up on just 1 or 2 keywords
            for _ in range(int(num_samples_per_role * 0.2)):
                skill = random.choice(required_skills)
                bad_templates = [
                    f"Looking for {role} job. Know {skill}.",
                    f"{role}. {skill}.",
                    f"I want to be a {role}.",
                    f"Worked with {skill} for 2 years."
                ]
                data.append([random.choice(bad_templates), role])

    # Shuffle dataset
    random.shuffle(data)
    
    # Save to CSV
    output_path = "data/synthetic_resumes.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        writer.writerows(data)
        
    print(f"Successfully generated {len(data)} samples at {output_path}")

if __name__ == "__main__":
    generate_synthetic_data()
