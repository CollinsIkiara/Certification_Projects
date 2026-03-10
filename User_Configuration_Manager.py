# User Configuration Manager

def add_setting(settings, key_value_pair):
    # Unpack the tuple into individual key and value variables
    key, value = key_value_pair

    # Convert key and value to lowercase for consistent storage and comparison
    key = key.lower()
    value = value.lower()

    # Check if the key already exists in the settings dictionary
    if key in settings:
        # Return an error message if the setting already exists
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # If key does not exist, add the new key-value pair to the settings dictionary
    settings[key] = value
    # Return a success message confirming the setting was added
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, key_value_pair):
    # Unpack the tuple into individual key and value variables
    key, value = key_value_pair

    # Convert key and value to lowercase for consistent storage and comparison
    key = key.lower()
    value = value.lower()

    # Check if the key exists in the settings dictionary before updating
    if key in settings:
        # Update the existing setting with the new value
        settings[key] = value
        # Return a success message confirming the setting was updated
        return f"Setting '{key}' updated to '{value}' successfully!"

    # Return an error message if the key does not exist
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    # Normalize the key to lowercase for consistent comparison
    key = key.lower()

    # Check if the key exists in the settings dictionary before deleting
    if key in settings:
        # Remove the key-value pair from the settings dictionary
        del settings[key]
        # Return a success message confirming the setting was deleted
        return f"Setting '{key}' deleted successfully!"

    # Return an error message if the key was not found
    return "Setting not found!"


def view_settings(settings):
    # Return early with a message if the settings dictionary is empty
    if not settings:
        return "No settings available."

    # Start the output with a header line
    lines = ["Current User Settings:"]

    # Iterate over each key-value pair and format it for display
    for key, value in settings.items():
        # Capitalize the first letter of the key for readability
        lines.append(f"{key.capitalize()}: {value}")

    # Join all lines with newlines and add a trailing newline at the end
    return "\n".join(lines) + "\n"


# Test dictionary with sample user configuration preferences
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}

# Test add_setting: should fail as 'theme' key already exists
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))

# Test add_setting: should succeed as 'volume' key does not exist
print(add_setting({'theme': 'light'}, ('volume', 'high')))

# Test update_setting: should succeed as 'theme' key exists
print(update_setting({'theme': 'light'}, ('theme', 'dark')))

# Test update_setting: should fail as 'volume' key does not exist
print(update_setting({'theme': 'light'}, ('volume', 'high')))

# Test delete_setting: should succeed as 'theme' key exists
print(delete_setting({'theme': 'light'}, 'theme'))

# Test view_settings: should display formatted output for a non-empty dictionary
print(view_settings({'theme': 'light'}))