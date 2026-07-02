import os
import subprocess
import sys

# Sudo management
def run_command(command, use_sudo=false):
    if use_sudo:
        command=f"sudo {command}"
    
    print("Running:")
    process=subprocess.run(command, shell=True)

    if process.returncore != 0:
        print("Error while processing. Exiting setup")

# Initialization
def main():
    print("Starting the script.. Standby..")

# Dependency Initialization
    print(" [1/4] - Installing dependencies.. Standby..")
    dependencies=("git cmake extra-cmake-modules kwin6-devel plasma6-dev qt6-base-devel qt6-declarative-devel qt6-quickcomponents-devel kf6-extra-cmake-modules kf6-kwindowsystem-devel kf6-kcoreaddons-devel kf6-kconfig-devel")

    run_command(f"zypper in -y {dependencies}", use_sudo=True)

# Cloning the KDE-Rounded_corners repository
    print(" [2/4] Cloning into git repo - KDE-Rounded_corners.. Standby..")

    repo_url="https://github.com/matinlotfali/KDE-Rounded-Corners.git"
    repo_dir = "KDE-Rounded_corners"
    
# Removing old files if exists
    if os.path.exists(repo_dir):
        print("A directory seems to already exist. Removing it so new one can be created..")
        run_command(f"rm -rf {repo_dir}")

    run_command(f"git clone {repo_url}")

# Repo file building and installation
    print(" [3/4] Installing the cloned file.. Almost done..")
    os.chdir(repo_dir)
    os.makedirs("build", exist_ok=True)
    os.chdir("build")

    run_command("cmake ..")
    run_command("make")
    run_command("make install" , use_sudo=True)

# Reload KWin
    print(" [4/4] Installation complete. Reloading Kwin..")
    
    try:
        configure_result = run_command("qdbus6 org.kde.Kwin /Kwin reconfigure")

        if configure_result = false:
            print ("Error while reconfiguring Kwin")
            print("But the installation is done properly")
            print("Go to System setting -> Desktop Effects and enable it manually")
        else:
            print("Configuration complete..")


if __name__ == "__main__":
    main()



    












