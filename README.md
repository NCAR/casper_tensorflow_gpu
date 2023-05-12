# Setup tensorflow 2.12 on casper

This package provides scripts to setup [Tensorflow 2.12](tf_pip) or [Tensorflow 2.11 without using `pip`](tf_nopip) with GPU support on casper without using any outside cuda modules.
The key steps for setting up tensorflow are to first install the correct versions of cudatoolkit and cudnn. 
Second, environment variables need to be set correctly to point tensorflow to the conda-based cuda installation.
Third, the `XLA_FLAGS` environment variable needs to be set to include the path to the conda environment. 

## Setup

1. Install miniconda 
2. Run `sh setup_conda_tf.sh` in [tf_pip for v2.12](tf_pip) or [tf_nopip for v2.11](tf_nopip) to create a conda environment with tensorflow and the appropriate libraries and environment variables.
3. Start a batch job on a gpu node. You can start a 30 minute testing job with `execcasper -A $PROJECT_ID -l select=1:ncpus=1:mem=20GB:ngpus=1 --gpu_type=v100 -q gpudev` 
4. Activate the environment with `conda activate tf212gpu` or `conda activate tf211gpu`. 
5. Run `python test_simple_nn.py` to test that the GPU is detected correctly and that a simple neural net will train on the GPU. 
