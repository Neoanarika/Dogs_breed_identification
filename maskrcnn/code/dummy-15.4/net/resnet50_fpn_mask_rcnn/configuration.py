from common import *
import configparser


class Configuration(object):

    def __init__(self):
        super(Configuration, self).__init__()
        self.version='configuration version \'mask-rcnn-resnet50-fpn, kaggle\''

        #net
        self.num_classes = 2 #include background class

        #rpn
        self.rpn_scales             = [ 1,  2,  4,  8 ]
        self.rpn_base_apsect_ratios = [1, 0.5,  2]
        self.rpn_base_sizes  = [ 8, 16, 32, 64 ] #diameter


        self.rpn_train_batch_size     = 128  # rpn target  256
        self.rpn_train_fg_fraction    = 0.5
        self.rpn_train_bg_thresh_high = 0.3
        self.rpn_train_fg_thresh_low  = 0.7

        self.rpn_train_nms_overlap_threshold  = 0.7 # rpn nms
        self.rpn_train_nms_min_size   =  5
        self.rpn_train_nms_pre_top_n  =  8192
        self.rpn_train_nms_post_top_n =  1024
        self.rpn_train_nms_pre_score_threshold = 0.5

        self.rpn_test_nms_overlap_threshold  = 0.7
        self.rpn_test_nms_min_size   =  5
        self.rpn_test_nms_pre_top_n  =  4096
        self.rpn_test_nms_post_top_n =  1024
        self.rpn_test_nms_pre_score_threshold = 0.5

        #crop
        self.pool_size = 14
        self.rcnn_select_size_thresholds = [
          [  0,    8],#'stride  1':
          [  8,   16],#'stride  2':
          [ 16,   32],#'stride  4':
          [ 32,  1e8],#'stride  8':
        ]

        #rcnn
        self.rcnn_train_batch_size      = 128  # rcnn target
        self.rcnn_train_fg_fraction     = 0.25
        self.rcnn_train_bg_thresh_high  = 0.5
        self.rcnn_train_bg_thresh_low   = 0.0
        self.rcnn_train_fg_thresh_low   = 0.5
        # self.rcnn_train_delta_norm_stds = (0.1, 0.1, 0.2, 0.2) #(1, 1, 1, 1) # <todo>
        self.rcnn_train_min_size = 6

        self.rcnn_train_nms_pre_score_threshold = 0.05
        self.rcnn_train_nms_overlap_threshold   = 0.8  # high for more proposals for mask
        self.rcnn_train_nms_min_size = 6

        self.rcnn_test_nms_pre_score_threshold = 0.1
        self.rcnn_test_nms_overlap_threshold   = 0.5
        self.rcnn_test_nms_min_size = 6

        #mask
        self.mask_size = 28
        self.mask_train_fg_thresh_low = 0.5
        self.mask_train_min_size = 6

        self.mask_test_nms_threshold = 0.5
        self.mask_test_threshold = 0.5
        self.mask_test_min_size  = 7




    def __repr__(self):
        raise NotImplementedError

    def save(self, file):
        raise NotImplementedError

    def load(self, file):
        raise NotImplementedError




# main #################################################################
if __name__ == '__main__':
    print( '%s: calling main function ... ' % os.path.basename(__file__))

    os.makedirs('/root/share/project/ellen-object-detect/results/xxx/',exist_ok=True)
    file='/root/share/project/ellen-object-detect/results/xxx/configure'

    cfg = Configuration()
    cfg.save(file)
    cfg.load(file)
    cfg.save('/root/share/project/ellen-object-detect/results/xxx/configure1')



