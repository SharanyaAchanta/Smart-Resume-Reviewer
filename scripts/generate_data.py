import json
import random
import csv
import os
import time
import hashlib
from collections import defaultdict

os.makedirs("data", exist_ok=True)

RANDOM_SEED = os.getenv("RANDOM_SEED")
if RANDOM_SEED is not None:
    try:
        random.seed(int(RANDOM_SEED))
    except ValueError:
        random.seed(RANDOM_SEED)

def load_job_roles():
    try:
        with open("utils/job_roles.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: utils/job_roles.json not found.")
        return {}

def _hash(text):
    return hashlib.md5(text.strip().lower().encode("utf-8")).hexdigest()

def generate_synthetic_data(num_samples_per_role=100):
    job_roles = load_job_roles()
    data = []
    seen = set()
    stats = defaultdict(int)
    started_at = time.time()

    print("Generating extended synthetic data...")

    for category, roles in job_roles.items():
        for role, details in roles.items():
            required_skills = details.get("required_skills", []) or []
            description = details.get("description", "")

            if not required_skills:
                continue

            for _ in range(num_samples_per_role):
                k = min(len(required_skills), random.randint(3, max(3, len(required_skills))))
                selected_skills = random.sample(required_skills, k=k)
                random.shuffle(selected_skills)

                templates = [
                    f"Experienced {role} with a strong background in {', '.join(selected_skills)}.",
                    f"Seeking a position as a {role}. Proficient in {', '.join(selected_skills)}.",
                    f"Skilled in {', '.join(selected_skills)}. {description}.",
                    f"History of working as a {role} handling {description}.",
                    f"Passionate about {category} and {role} roles. Core competencies: {', '.join(selected_skills)}.",
                    f"As a {role}, I have deployed systems using {selected_skills[0]} and {selected_skills[1]}.",
                    f"Resume: {role}. Skills: {', '.join(selected_skills)}."
                ]

                text = random.choice(templates)

                if random.random() > 0.7:
                    text += " Proven track record of success in agile environments."

                if random.random() > 0.85:
                    text = text.replace(".", "").strip() + "."

                h = _hash(text)
                if h in seen:
                    continue
                seen.add(h)

                data.append([text, role])
                stats[role] += 1

            for _ in range(int(num_samples_per_role * 0.2)):
                skill = random.choice(required_skills)
                bad_templates = [
                    f"Looking for {role} job. Know {skill}.",
                    f"{role}. {skill}.",
                    f"I want to be a {role}.",
                    f"Worked with {skill} for 2 years."
                ]
                text = random.choice(bad_templates)

                h = _hash(text)
                if h in seen:
                    continue
                seen.add(h)

                data.append([text, role])
                stats[role] += 1

    random.shuffle(data)

    output_path = "data/synthetic_resumes.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        writer.writerows(data)

    manifest = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_samples": len(data),
        "roles": dict(stats),
        "seed": RANDOM_SEED,
        "output": output_path,
        "generation_time_sec": round(time.time() - started_at, 3)
    }

    with open("data/manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Successfully generated {len(data)} samples at {output_path}")
    print("Dataset manifest written to data/manifest.json")

if __name__ == "__main__":
    generate_synthetic_data()
