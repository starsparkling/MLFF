isCalcFeat = False
isFitLinModel = False
isClassify = False
isRunMd = False
isRunMd_nn = False
isFollowMd = False
isFitVdw = False
isRunMd100_nn = False
isRunMd100 = False
isNewMd100 = False
codedir = '/home/wuxingxing/codespace/MLFF_ekf'
atomType = [29]
use_Ftype = [1, 2]
nFeatures = 42
use_GKalman = True
is_scale = True
storage_scaler = True
itype_Ei_mean = [166.4]
n_epoch = 80
torch = <module 'torch' from '/home/wuxingxing/anaconda3/envs/mlff_env/lib/python3.9/site-packages/torch/__init__.py'>
F = <module 'torch.nn.functional' from '/home/wuxingxing/anaconda3/envs/mlff_env/lib/python3.9/site-packages/torch/nn/functional.py'>
add_force = False
is_nn_do_profile = False
isNNpretrain = False
isNNfinetuning = True
train_data_path = './train_data/final_train'
test_data_path = './train_data/final_test'
f_train_dR_neigh = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/dR_neigh_train.csv'
f_test_dR_neigh = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/dR_neigh_test.csv'
dR_neigh = False
DCNLayers = 5
torch_dtype = 'float64'
feature_dtype = 'float64'
training_dtype = 'float64'
inference_dtype = 'float64'
imodel = 1
md_num_process = 1
is_md100_egroup = False
is_md100_show_X11_fig = False
prefix = './'
trainSetDir = '/home/wuxingxing/codespace/MLFF_ekf/PWdata'
fortranFitSourceDir = '/home/liuliping/program/nnff/git_version/src/fit'
fitModelDir = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat'
mdImageFileDir = './MD'
PWmatDir = '/home/buyu/PWmat/MDAlHsml3_loop'
pbc = True
dRneigh_path = './PWdata/dRneigh.dat'
dp_predict = False
DP_cfg_dp = {'embeding_net': {'network_size': [25, 50, 100], 'bias': True, 'resnet_dt': False, 'activation': <built-in method tanh of type object at 0x2b170776ff80>}, 'fitting_net': {'network_size': [240, 240, 240, 1], 'activation': <built-in method tanh of type object at 0x2b170776ff80>, 'resnet_dt': True, 'bias': True}}
DP_cfg_dp_kf = {'embeding_net': {'network_size': [25, 25, 25], 'bias': True, 'resnet_dt': False, 'activation': <built-in method tanh of type object at 0x2b170776ff80>}, 'fitting_net': {'network_size': [50, 50, 50, 1], 'activation': <built-in method tanh of type object at 0x2b170776ff80>, 'resnet_dt': True, 'bias': True}}
maxNeighborNum = 100
iflag_PCA = 0
Rc_M = 6.0
Rc_min = 5.8
Ftype_name = {1: 'gen_2b_feature', 2: 'gen_3b_feature', 3: 'gen_2bgauss_feature', 4: 'gen_3bcos_feature', 5: 'gen_MTP_feature', 6: 'gen_SNAP_feature', 7: 'gen_deepMD1_feature', 8: 'gen_deepMD2_feature'}
use_LKalman = False
use_SKalman = False
use_storage_scaler = False
batch_size = 1
nfeat_type = 2
Ftype1_para = {'numOf2bfeat': [24, 24, 24, 24, 24, 24, 24, 24, 24, 24], 'Rc': [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0], 'Rm': [5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8], 'iflag_grid': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'fact_base': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], 'dR1': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 'iflag_ftype': 3}
Ftype2_para = {'numOf3bfeat1': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'numOf3bfeat2': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'Rc': [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0], 'Rc2': [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0], 'Rm': [5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8], 'iflag_grid': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'fact_base': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], 'dR1': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 'dR2': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 'iflag_ftype': 3}
Ftype3_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'n2b': [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'w': [1.0, 1.5, 2.0]}
Ftype4_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'n3b': [20, 20, 20, 20, 20, 20, 20, 20, 20, 20], 'zeta': [[1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0], [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0]], 'w': [[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]]}
Ftype5_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'Rm': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 'n_MTP_line': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'tensors': [['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )'], ['1, 4, 0, ( )                              ', '2, 3,3, 0,0, ( ), ( )                     ', '2, 3,3, 1,1, ( 21 ), ( 11 )               ', '2, 3,3, 2,2, ( 21, 22 ), ( 11, 12 )       ', '3, 2,2,2, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 3,3,3, 2,1,1 ( 21, 31 ), ( 11 ), ( 12 )', '3, 2,2,2, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 3,3,3, 3,2,1 ( 21, 22, 31 ), ( 11, 12 ), ( 13 )', '3, 2,2,2, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '3, 3,3,3, 4,2,2 ( 21, 22, 31, 32 ), ( 11, 12 ), ( 13, 14 )', '4, 2,2,2,2 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 3,3,3,3 3,1,1,1 ( 21, 31, 41 ), ( 11 ), ( 12 ), ( 13 )', '4, 2,2,2,2 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )', '4, 3,3,3,3 4,2,1,1 ( 21, 22, 31, 41 ), ( 11, 12 ), ( 13 ), ( 14 )']]}
Ftype6_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'J': [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0], 'n_w_line': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'w1': [[0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4], [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4]], 'w2': [[0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6], [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6]]}
Ftype7_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'Rc2': [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0], 'Rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'M': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'weight_r': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}
Ftype8_para = {'Rc': [5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4], 'M': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 'weight_r': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'w': [1.0, 1.5, 2.0, 2.5]}
kfnn_trainEtot = True
kfnn_trainEi = False
kfnn_trainForce = True
E_tolerance = 0.3
recalc_grid = 1
rMin = 0.0
kernel_type = 2
use_lpp = False
lppNewNum = 3
lpp_n_neighbors = 5
lpp_weight = 'adjacency'
lpp_weight_width = 1.0
alpha0 = 1.0
k_dist0 = 0.01
DesignCenter = False
ClusterNum = [3, 2]
fortranFitAtomRepulsingEnergies = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
fortranFitAtomRadii = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
fortranFitWeightOfEnergy = 0.0
fortranFitWeightOfEtot = 0.5
fortranFitWeightOfForce = 0.5
fortranFitRidgePenaltyTerm = 0.0001
fortranFitDwidth = 3.0
mdCalcModel = 'lin'
mdRunModel = 'nvt'
mdStepNum = 10
mdStepTime = 1
mdStartTemperature = 300
mdEndTemperature = 300
mdNvtTaut = 100.0
mdOptfmax = 0.05
mdOptsteps = 10
isTrajAppend = False
isNewMovementAppend = False
mdTrajIntervalStepNum = 50
mdLogIntervalStepNum = 10
mdNewMovementIntervalStepNum = 10
mdStartImageIndex = 0
isOnTheFlyMd = False
isFixedMaxNeighborNumForMd = False
mdMaxNeighborNum = None
isMdCheckVar = False
isReDistribute = True
velocityDistributionModel = 'MaxwellBoltzmann'
isMdProfile = False
gpu_mem = 0.9
cuda_dev = '0'
cupyFeat = True
tf_dtype = 'float32'
test_ratio = 0.2
activation_func = 'softplus'
ntypes = 1
nLayers = 3
nNodes = np.array([[15, 15], [15, 15], [1, 1]])
b_init = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
dwidth = 3.0
train_continue = False
progressbar = False
flag_plt = False
train_stage = 1
train_verb = 0
learning_rate = 0.001
rtLossE = 0.8
rtLossF = 0.2
rtLossEtot = 0.2
bias_corr = True
epochs_alltrain = 1001
epochs_Fi_train = 11
iFi_repeat = 1
eMAE_err = 0.01
fMAE_err = 0.02
isDynamicFortranFitRidgePenaltyTerm = False
fortranGrrRefNum = [800, 1000]
fortranGrrRefNumRate = 0.1
fortranGrrRefMinNum = 1000
fortranGrrRefMaxNum = 3000
fortranGrrKernelAlpha = 1
fortranGrrKernalDist0 = 3.0
realFeatNum = 111
fbinListPath = '/home/wuxingxing/codespace/MLFF_ekf/PWdata/location'
sourceFileList = []
InputPath = '/home/wuxingxing/codespace/MLFF_ekf/input'
OutputPath = '/home/wuxingxing/codespace/MLFF_ekf/output'
Ftype1InputPath = './input/gen_2b_feature.in'
Ftype2InputPath = './input/gen_3b_feature.in'
FtypeiiInputPath = {1: './input/gen_2b_feature.in', 2: './input/gen_3b_feature.in', 3: './input/gen_2bgauss_feature.in', 4: './input/gen_3bcos_feature.in', 5: './input/gen_MTP_feature.in', 6: './input/gen_SNAP_feature.in', 7: './input/gen_deepMD1_feature.in', 8: './input/gen_deepMD2_feature.in'}
i = 8
featCollectInPath = './fread_dfeat/feat_collect.in'
fitInputPath_lin = './fread_dfeat/fit_linearMM.input'
fitInputPath2_lin = '/home/wuxingxing/codespace/MLFF_ekf/input/fit_linearMM.input'
featCollectInPath2 = '/home/wuxingxing/codespace/MLFF_ekf/input/feat_collect.in'
linModelCalcInfoPath = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/linear_feat_calc_info.txt'
linFitInputBakPath = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/linear_fit_input.txt'
f_atoms = './MD/atom.config'
atomTypeNum = 1
nFeats = np.array([111, 111, 111])
dir_work = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/'
f_train_feat = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/feat_train.csv'
f_test_feat = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/feat_test.csv'
f_train_natoms = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/natoms_train.csv'
f_test_natoms = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/natoms_test.csv'
f_train_dfeat = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/dfeatname_train.csv'
f_test_dfeat = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/dfeatname_test.csv'
f_train_force = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/force_train.csv'
f_test_force = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/force_test.csv'
f_train_egroup = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/egroup_train.csv'
f_test_egroup = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/egroup_test.csv'
f_train_ep = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/ep_train.csv'
f_test_ep = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/ep_test.csv'
d_nnEi = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNEi/'
d_nnFi = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNFi/'
f_Einn_model = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNEi/allEi_final.ckpt'
f_Finn_model = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNFi/Fi_final.ckpt'
f_data_scaler = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNFi/data_scaler.npy'
f_Wij_np = '/home/wuxingxing/codespace/MLFF_ekf/fread_dfeat/NN_output/NNFi/Wij.npy'
MLFF_dmirror_cfg = [('linear', 42, 1, True)]
MLFF_dmirror_cfg1 = [('linear', 42, 30, True), ('activation',), ('linear', 30, 60, True), ('activation',), ('linear', 60, 1, True)]
MLFF_dmirror_cfg2 = [('linear', 42, 1, True), ('activation',), ('linear', 1, 1, True)]
MLFF_dmirror_cfg3 = [('linear', 42, 10, True), ('activation',), ('linear', 10, 3, True), ('activation',), ('linear', 3, 1, True)]
