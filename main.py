import shutil
import sys

# Adding the path to Pyke to the system path
sys.path.append(r"D:\Downloads\pyke3")
from pyke import knowledge_engine, krb_traceback

# Path to the directory you want to remove
folder_path = r'D:\Downloads\pyke3\ESS\compiled_krb'

# Remove the folder and all its contents
try:
    shutil.rmtree(folder_path)
    print("Folder and all its contents removed successfully")
except Exception as error:
    print(f"Error: {error}")


# Print the directory from where the engine is loading files
print(f"Loading KB from: {__file__}")

engine = knowledge_engine.engine(__file__)

engine.reset()

print("Activating knowledge base...")
engine.activate('rules')

print("Proving goal...")
try:
    with engine.prove_goal(
            'rules.dermatology_advice($advice)') as gen:
        found = False
        for vars, plan in gen:
            print()
            print("You should: %s" % (vars['advice']))
            found = True
        if not found:
            print("No advice generated.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    krb_traceback.print_exc()
    sys.exit(1)

print()
print("Done")
