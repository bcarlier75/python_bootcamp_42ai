# This script will create the package ai42.
# To install the package you will need to run 'pip install ./dist/ai42-1.0.0.tar.gz'

if [ -d "ai42" ]
then
  rm -rf ai42
  mkdir ai42
  'Directory ai42 removed and created...'
else
  mkdir ai42
  echo 'Directory ai42 created...'
fi
echo 'Copying necessary files in ai42 directory...'
cp __init__.py ai42
mkdir ai42/logging
cp __init__.py ai42/logging
cp log.py ai42/logging
echo 'Upgrading setuptools and wheel if necessary...'
pip install --upgrade setuptools wheel
echo 'Creating package...'
python setup.py sdist bdist_wheel
