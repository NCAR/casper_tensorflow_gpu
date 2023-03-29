export OLD_LD_LIBRARY_PATH=${LD_LIBRARY_PATH}
export CUDNN_PATH=${CONDA_PREFIX}/lib/python3.10/site-packages/nvidia/cudnn
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CONDA_PREFIX}/lib/:${CUDNN_PATH}/lib
export XLA_FLAGS=--xla_gpu_cuda_data_dir=${CONDA_PREFIX}
