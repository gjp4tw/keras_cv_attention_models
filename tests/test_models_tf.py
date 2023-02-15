import pytest
from skimage.data import chelsea

import sys

sys.path.append(".")
import keras_cv_attention_models
from keras_cv_attention_models.backend import models

""" Recognition models Coat / HaloNet / HorNet / NFNet / VOLO defination """


def test_CoaT_defination():
    mm = keras_cv_attention_models.coat.CoaTLiteMini(pretrained=None)
    assert isinstance(mm, models.Model)

    mm = keras_cv_attention_models.coat.CoaTLiteSmall(pretrained=None, num_classes=0)
    assert isinstance(mm, models.Model)


def test_HaloNet_defination():
    mm = keras_cv_attention_models.halonet.HaloNetH0(pretrained=None)
    assert isinstance(mm, models.Model)

    mm = keras_cv_attention_models.halonet.HaloNetH2(pretrained=None, num_classes=0)
    assert isinstance(mm, models.Model)


def test_HorNet_defination():
    mm = keras_cv_attention_models.hornet.HorNetSmall(pretrained=None)
    assert isinstance(mm, models.Model)

    mm = keras_cv_attention_models.hornet.HorNetSmallGF(pretrained=None, num_classes=0)
    assert isinstance(mm, models.Model)


def test_NFNet_defination():
    mm = keras_cv_attention_models.nfnets.NFNetF0(pretrained=None)
    assert isinstance(mm, models.Model)

    mm = keras_cv_attention_models.nfnets.ECA_NFNetL1(pretrained=None, num_classes=0)
    assert isinstance(mm, models.Model)


def test_VOLO_defination():
    mm = keras_cv_attention_models.volo.VOLO_d3(pretrained=None)
    assert isinstance(mm, models.Model)

    mm = keras_cv_attention_models.volo.VOLO_d4(pretrained=None, num_classes=0)
    assert isinstance(mm, models.Model)


""" Recognition models Coat / EfficientNetV2B1_preprocessing / HaloNet / HorNet / NAT / VOLO prediction """


def test_CoaT_new_shape_predict():
    mm = keras_cv_attention_models.coat.CoaTLiteMini(input_shape=(193, 117, 3), pretrained="imagenet")
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


def test_EfficientNetV2B1_preprocessing_predict():
    mm = keras_cv_attention_models.efficientnet.EfficientNetV2B1(pretrained="imagenet", include_preprocessing=True)
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


def test_HaloRegNetZB_predict():
    mm = keras_cv_attention_models.halonet.HaloRegNetZB(pretrained="imagenet")
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


def test_HorNetTinyGF_new_shape_predict():
    mm = keras_cv_attention_models.hornet.HorNetTinyGF(input_shape=(174, 255, 3), pretrained="imagenet")
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


def test_NAT_Mini_new_shape_predict():
    mm = keras_cv_attention_models.nat.NAT_Mini(input_shape=(174, 255, 3), pretrained="imagenet")
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


def test_VOLO_d1_new_shape_predict():
    mm = keras_cv_attention_models.volo.VOLO_d1(input_shape=(512, 512, 3), pretrained="imagenet")
    pred = mm(mm.preprocess_input(chelsea()))  # Chelsea the cat
    out = mm.decode_predictions(pred)[0][0]

    assert out[1] == "Egyptian_cat"


""" Detection models with dynamic input_shape """


def test_EfficientDetD1_dynamic_predict():
    mm = keras_cv_attention_models.efficientdet.EfficientDetD1(input_shape=(None, None, 3), pretrained="coco")
    input_shape = (376, 227, 3)
    pred = mm(mm.preprocess_input(chelsea(), input_shape=input_shape))  # Chelsea the cat
    assert pred.shape == (1, 16641, 94)

    pred_label = mm.decode_predictions(pred, input_shape=input_shape)[0][1].numpy()
    assert keras_cv_attention_models.coco.data.COCO_90_LABEL_DICT[pred_label[0]] == "cat"


def test_EfficientDetLite1_dynamic_predict():
    mm = keras_cv_attention_models.efficientdet.EfficientDetLite1(input_shape=(None, None, 3), pretrained="coco")
    input_shape = (376, 227, 3)
    pred = mm(mm.preprocess_input(chelsea(), input_shape=input_shape))  # Chelsea the cat
    assert pred.shape == (1, 16641, 94)

    pred_label = mm.decode_predictions(pred, input_shape=input_shape)[0][1].numpy()
    assert keras_cv_attention_models.coco.data.COCO_90_LABEL_DICT[pred_label[0]] == "cat"


def test_YOLOR_CSP_dynamic_predict():
    mm = keras_cv_attention_models.yolor.YOLOR_CSP(input_shape=(None, None, 3), pretrained="coco")
    input_shape = (188, 275, 3)
    pred = mm(mm.preprocess_input(chelsea(), input_shape=input_shape))  # Chelsea the cat
    assert pred.shape == (1, 3330, 85)

    pred_label = mm.decode_predictions(pred, input_shape=input_shape)[0][1].numpy()
    assert keras_cv_attention_models.coco.data.COCO_80_LABEL_DICT[pred_label[0]] == "cat"


def test_YOLOXS_dynamic_predict():
    mm = keras_cv_attention_models.yolox.YOLOXS(input_shape=(None, None, 3), pretrained="coco")
    input_shape = (188, 276, 3)
    pred = mm(mm.preprocess_input(chelsea()[:, :, ::-1], input_shape=input_shape))  # Chelsea the cat
    assert pred.shape == (1, 1110, 85)

    pred_label = mm.decode_predictions(pred, input_shape=input_shape)[0][1].numpy()
    assert keras_cv_attention_models.coco.data.COCO_80_LABEL_DICT[pred_label[0]] == "cat"


def test_YOLOV7_Tiny_dynamic_predict():
    mm = keras_cv_attention_models.yolov7.YOLOV7_Tiny(input_shape=(None, None, 3), pretrained="coco")
    input_shape = (188, 276, 3)
    pred = mm(mm.preprocess_input(chelsea(), input_shape=input_shape))  # Chelsea the cat
    assert pred.shape == (1, 3330, 85)

    pred_label = mm.decode_predictions(pred, input_shape=input_shape)[0][1].numpy()
    assert keras_cv_attention_models.coco.data.COCO_80_LABEL_DICT[pred_label[0]] == "cat"
