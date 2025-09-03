# Model Card: SmartNVR-PersonDet-INT8

**Owner**: Vision Team  
**Version**: 1.0.0  
**Date**: 2025-09-02

## 1. Overview & Intended Use
Real-time person detection for NVR edge devices; intended for surveillance analytics.

## 2. Training Data
COCO-derived with additional surveillance imagery; consent/TOU checked.

## 3. Evaluation
mAP@0.5=0.48; latency P95=12ms on ARC; safety evals pass thresholds.

## 4. Ethical Considerations
Bias monitored across lighting/skin tones; accessibility notes documented.

## 5. Limitations
Not for face recognition; not robust to heavy occlusion.

## 6. Deployment
Model monitoring and rollback plan defined.

## 7. Contact
vision-team@example.org
