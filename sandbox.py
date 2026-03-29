def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call}({function_call})")
    else:
        print(f" - Calling function: {function_call}")

    
    function_map = {
    "get_file_content": "a",
    "get_files_info": "b",
    "run_python_file": "c",
    "write_file": "d"
}
    
    function_name = function_call or ""

    if function_name not in function_map.keys():
        print("noob")
    else:
        print("good")


call_function("get_file_content", verbose=True)