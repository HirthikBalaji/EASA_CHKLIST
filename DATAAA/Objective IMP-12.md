**AI/ML Software Development Checklist**
==================================================

### Identity and Purpose

* Is the proposed learning assurance process described, including all steps from C.3.1.2 to C.3.1.14? [YES/NO]
* Has a plan for learning assurance been included, addressing all objectives from Section C.3 and detailing the proposed MOC? [YES/NO]

### Requirements and Architecture Management

* Have requirements for AI/ML constituent design been prepared?
	+ Are requirements refined through successive steps?
	+ Is there a traditional flow-down of requirements (e.g., from aircraft to system)?
* Can feature engineering or data labelling be automated (at least partially)? [YES/NO]

### Model Development and Verification

* Has the robustness of the trained model been verified in adverse conditions? [YES/NO]
* Have anticipated generalisation bounds using test data sets been verified? [YES/NO]
* Is a description of the resulting ML model provided? [YES/NO]
* Are verification activities for the trained model complete? [YES/NO]

### Model Implementation and Transformation

* Are requirements pertaining to the ML model implementation process captured? [YES/NO]
* Has the model description been validated, along with each requirement captured under Objective IMP-01?
* Is evidence provided that all derived requirements generated through the model implementation process have been provided to (sub)system processes, including safety assessment? [YES/NO]
* Are post-training model transformations (conversion, optimisation) identified and validated for their impact on model behaviour and performance? [YES/NO]
* Have any necessary software tools and hardware environments for model transformation been identified? [YES/NO]

### Development Assurance Process

* Has a plan been executed to develop the inference model into software and/or hardware items? [YES/NO]
* Are differences between training and verification platforms assessed for their possible impact on inference model behaviour and performance? [YES/NO]
* Is the stability of the inference model verified? [YES/NO]
* Is the robustness of the inference model in adverse conditions verified? [YES/NO]
* Has requirements-based verification of the inference model behavior when integrated into the AI/ML constituent been performed? [YES/NO]
* Are AI/ML constituent verification activities complete? [YES/NO]

**Reviewer's Checklist**

* Verify that the author has completed all tasks listed above.
* Confirm that the author has provided evidence to support their claims.