

def get_environment_variable(*args, **kwargs):
    """Mock function to return env variable."""
    var = None
    default = None

    # import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
    var = args[0]
    if len(args) == 2:
        default = args[1]

    if var == "HOME":
        value = "/home/robot/"
    else:
        value = None
        if default:
            value = default

    return value
