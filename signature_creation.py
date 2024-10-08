import keyword
from nanorpc.versions.handler import NodeVersion, get_commands_for_version


# This script creates the resulting typed python signatures form the  COMMANDS = { ... }

# MODIFY NODE_VERSION HERE
NODE_VERSION = NodeVersion.V27_1


def is_valid_command_structure(command_details):
    expected_keys = {"required", "optional"}
    actual_keys = set(command_details.keys())
    return actual_keys == expected_keys


def append_underscore_if_keyword(arg):
    """Appends an underscore to the argument if it's a Python reserved keyword."""
    return arg + "_" if keyword.iskeyword(arg) else arg


def generate_method_signatures(input_path):
    try:
        commands_dict = get_commands_for_version(NODE_VERSION)

    except ValueError as e:
        print(e)
        return

    output_file_path = str(NODE_VERSION).replace(
        "NodeVersion.", "").lower() + "_signatures.py"

    with open(output_file_path, 'w') as output_file:
        for command_name, command_details in commands_dict.items():
            # if not is_valid_command_structure(command_details):
            #     print(f"Skipping '{command_name}': Invalid command structure.")
            #     continue

            required_params = [append_underscore_if_keyword(
                arg) for arg in command_details.get("required", [])]
            optional_params = [append_underscore_if_keyword(
                arg) for arg in command_details.get("optional", [])]

            params = required_params + \
                [f'{param}=None' for param in optional_params]
            params_string = ", ".join(params)

            # Generate kwargs string for optional parameters
            kwargs_string = ", ".join(
                [f"{param}={param}" for param in optional_params])

            # Combine required params and kwargs string for the method call
            method_call_params = ', '.join(
                required_params + ([kwargs_string] if kwargs_string else []))

            method_signature = (
                f"async def {command_name}(self, {params_string}):\n"
                f"    return await self.rpc.{
                    command_name}({method_call_params})\n\n"
            )
            output_file.write(method_signature)

    print(f"Method signatures written to {output_file_path}")


# Example usage
generate_method_signatures(NODE_VERSION)
