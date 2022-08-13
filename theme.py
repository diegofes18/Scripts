import json,sys,argparse,yaml,toml
from yaml.loader import SafeLoader

parser = argparse.ArgumentParser(description = "Python Script to change the "+
         "qtile theme from the json file")
parser.add_argument ("-t","--theme", help="dark-grey, dracula, material-darker"+
        ", material-ocean, monokai-pro, nord-wave, nord, onedark, jungle")
args = parser.parse_args()

def main(argv):
    path = "/home/diegofes/.config/qtile/"
    theme = args.theme

    with open(path+"config.json","r") as jsonFile:
        data = json.load(jsonFile)

    data["theme"] = theme  

    with open(path+"config.json","w") as jsonFile:
        json.dump(data, jsonFile)

    print("theme changed to: " + theme)
    
    #onedark-
    if (theme == "onedark"):
        with open("/home/diegofes/.config/starship.toml","r") as f:
            data = toml.load(f)
    
        data['directory']['format'] = '[ diegofes ❯](bold fg:#E06C75) [\uf07c $path](bold fg:#61AFEF)[$read_only]($read_only_style) '


        with open("/home/diegofes/.config/starship.toml","w") as jsonFile:
            toml.dump(data, jsonFile)
    
    #material-ocean
    if (theme == "material-ocean"):
        with open("/home/diegofes/.config/starship.toml","r") as f:
            data = toml.load(f)
    
        data['directory']['format'] = '[ diegofes ❯](bold fg:#de8817 ) [\uf07c $path](bold fg:#fac746 )[$read_only]($read_only_style) '


        with open("/home/diegofes/.config/starship.toml","w") as jsonFile:
            toml.dump(data, jsonFile) 
     #dracula   
    if (theme == "dracula"):
        with open("/home/diegofes/.config/starship.toml","r") as f:
            data = toml.load(f)
    
        data['directory']['format'] = '[ diegofes ❯](fg:196) [\uf07c $path]($style)[$read_only]($read_only_style) '


        with open("/home/diegofes/.config/starship.toml","w") as jsonFile:
            toml.dump(data, jsonFile)         
    if (theme == "nord"):
        with open("/home/diegofes/.config/starship.toml","r") as f:
            data = toml.load(f)
    
        data['directory']['format'] = '[ diegofes ❯](fg:196) [\uf07c $path]($style)[$read_only]($read_only_style) '


        with open("/home/diegofes/.config/starship.toml","w") as jsonFile:
            toml.dump(data, jsonFile)      
    
    if (theme == "jungle"):
        with open("/home/diegofes/.config/starship.toml","r") as f:
            data = toml.load(f)
    
        data['directory']['format'] = '[ diegofes ❯](fg:196) [\uf07c $path]($style)[$read_only]($read_only_style) '


        with open("/home/diegofes/.config/starship.toml","w") as jsonFile:
            toml.dump(data, jsonFile)        
    

if __name__ == "__main__":
    main(args)
