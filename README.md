# Setup TensorFlow on Casper

This package provides scripts to setup [Tensorflow using `pip`](tf_pip) or [Tensorflow without using `pip`](tf_nopip) with GPU support on casper without using any outside CUDA modules.
The key steps for setting up TensorFlow are to first install the correct versions of `cudatoolkit` and `cudnn` packages using the Casper `conda` module. 'tensorrt' is also installed for the `pip` version. 
Second, environment variables need to be set correctly to point TensorFlow to the conda-based CUDA installation and associated libraries. These are set during the activation of each conda environment.
Third, the `XLA_FLAGS` environment variable needs to be set to include the path to the conda environment.

## Setup

1. (Optional) Install [MiniConda](https://docs.conda.io/en/latest/miniconda.html) or [MambaForge](https://github.com/conda-forge/miniforge) to your local machine if not running on Casper. 
2. `cd` to `tf_pip` or `tf_nopip` depending on desire to use TensorFlow installed with pip or installed from `conda-forge` channel.
3. Run `sh setup_conda_tfXXX.sh` where XXX is the version number in [tf_pip](tf_pip) or [tf_nopip](tf_nopip). This creates a conda environment with TensorFlow and the appropriate libraries and environment variables.
4. Start a batch job on a gpu node. You can start a 30 minute testing job with `execcasper -l select=1:ncpus=1:mem=20GB:ngpus=1 --gpu_type=v100 -q gpudev -A $PROJECT_ID` 
5. Activate the environment with `module load conda` and `conda activate tfXXXgpu`. 
6. Run `python test_simple_nn.py` to test that the GPU is detected correctly and that a simple neural net will train on the GPU. 
