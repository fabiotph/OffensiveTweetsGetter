
# Values list:
#     "'<text>' <count> <[optional] exact>" 

#     - text: text to search
#     - count: number of total results
#     - exact: if "false" or "False" not search perfect match
    
# Examples:
#     "'bom dia' 10": search 10 tweets with "bom dia"
#     "'bom dia' 10 false": search 1o tweets with "bom" and "dia"


list=(
    "'bom dia' 10"
    "'bom dia' 10 false"
)

exec_file="python3 main.py"

for args in "${list[@]}"; do
    eval "${exec_file} ${args}"
done
