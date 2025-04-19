import json
import os

def filter_json(input_file, output_file, condition):
    """
    Reads a JSON file, filters entries based on a condition, 
    and writes the filtered entries to a new JSON file.

    :param input_file: Path to the input JSON file.
    :param output_file: Path to the output JSON file.
    :param condition: A function that takes a JSON entry and returns True if it should be included.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        
        if not isinstance(data, list):
            raise ValueError("The JSON file must contain a list of entries.")
        
        filtered_data = [entry for entry in data if condition(entry)]
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(filtered_data, outfile, ensure_ascii=False, indent=4)
        
        print(f"Filtered data saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example condition function
def example_condition(entry):
    # Check if 'image_path' contains the specified string
    return '/washington_post/images/0000/' in entry.get('image_path', '')

if __name__ == "__main__":
    input_path = "/mnt/data1/users/yiwei/data/origin/data.json"  # Replace with the path to your input JSON file
    output_path = "output.json"  # Replace with the desired output file path
    
    # Ensure the input file exists
    if not os.path.exists(input_path):
        print(f"Input file {input_path} does not exist.")
    else:
        filter_json(input_path, output_path, example_condition)
