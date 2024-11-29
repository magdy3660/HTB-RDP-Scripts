# HTB-RDP-Scripts
scripts for faster Access to targets when doing the labs

`git clone https://github.com/magdy3660/HTB-RDP-Scripts.git`
Ensure `~/bin` Exists**  
If the `~/bin` directory does not already exist, create it:
```
mkdir -p ~/bin`
``` 
- **Create the Symlinks**  
    Run the following commands to create the symlinks:
    
    `ln -s ~/rdp.py ~/bin/rdp ln -s ~/rdp.sh ~/bin/rdpsh`
    
- **Ensure the Scripts are Executable**  
    Make sure both scripts have executable permissions:
    `chmod +x ~/rdp.py chmod +x ~/rdp.sh`
    
- **Add `~/bin` to Your PATH**  
    If `~/bin` is not already in your `PATH`, add it by editing your shell configuration file (e.g., `.bashrc`, `.zshrc`):
    
    `echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc`
    
    Then reload the shell configuration:
    `source ~/.bashrc`
    
- **Test the Symlinks**  
    Run the following to test if the symlinks work:
    
    `rdp rdpsh`
