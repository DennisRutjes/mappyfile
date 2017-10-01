import mappyfile

def test():
    # START OF API EXAMPLE
    # load will accept a filename (loads will accept a string)
    mapfile = mappyfile.load("./docs/examples/raster.map")

    # print the map name
    print(mapfile["name"]) # "MyMap"
       
    # access layers
    layers = mapfile["layers"]
    layer2 = layers[1] # access by index
    
    # access classes in a layer
    classes = layer2["classes"]

    for c in classes:
        print(c["name"])
    # END OF API EXAMPLE
    assert(mapfile["name"] == 'MyMap')

if __name__ == "__main__":
    test()