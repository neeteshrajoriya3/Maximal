import yaml
from faker import Faker

fake=Faker()

project_key=fake.bothify("???").upper()
#print(k)
project_description = fake.sentence(nb_words=8)
print(project_description)
try:
    # ✅ Load config.yaml safely
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)  # ✅ Ensure config is loaded correctly

    if config is None:  # ❌ Handle case where file is empty or invalid
        config = {"jira": {"project": {}}}

    # ✅ Update the project key in config
    config["jira"]["project"]["key"] = project_key

    # ✅ Save the updated config back to config.yaml
    with open("config.yaml", "w") as file:
        yaml.safe_dump(config, file)

    print(f"✅ Updated config.yaml with new Project Key: {project_key}")

except FileNotFoundError:
    print("Error: config.yaml not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
except Exception as e:  # ✅ Catch any unexpected errors
    print(f"Unexpected error: {e}")