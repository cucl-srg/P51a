if [ -z $1 ]; then
        echo crsid argument is empty
        exit 1
fi
export CRSID=$1
cd /home/l51/$CRSID/
mkdir P51aLab2
cd /home/l51/$CRSID/P51aLab2
echo "now get the zip file, unpack it in "
pwd
echo " and build the code using the compile_all_user.sh script"
