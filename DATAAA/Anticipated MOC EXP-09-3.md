**Checklist for Author and Reviewer: AI/ML Software Development**
==========================

### IDENTITY AND PURPOSE

#### DQRs (Data Quality Requirements)

* Have you captured DQRs for all data required for training, testing, and verification of the AI/ML constituent?
	+ Yes / No
* Are the DQRs relevant to support the intended use?
	+ Yes / No
* Can you determine the origin of the data?
	+ Yes / No
* Have you specified requirements related to the annotation process?
	+ Yes / No
* What is the format, accuracy, and resolution of the data?
	+ [Insert details]
* Is the data traceable from its origin to its final operation through the whole pipeline?
	+ Yes / No
* Are there mechanisms ensuring that the data will not be corrupted while stored, processed, or transmitted?
	+ Yes / No
* Are the data sets complete and representative?
	+ Yes / No
* Is there a level of independence between training, validation, and test data sets?
	+ Yes / No

#### Data Relevance

* For each type of data representing an operating parameter of the AI/ML constituent:
	+ Is the accuracy of the data documented?
		- Yes / No
	+ Is the resolution of the data documented?
		- Yes / No
	+ Is the quality of annotated data documented?
		- Yes / No
	+ Is the integrity of the data (assurance that it has not been corrupted) documented?
		- Yes / No
	+ Are necessary manipulations of the data (e.g., anonymization) documented?
		- Yes / No

### Inference Model Verification

#### IMP-08: Performance Evaluation

* Have you performed an evaluation of the performance of the inference model based on the test data set?
	+ Yes / No
* Is the result of the model verification documented?
	+ Yes / No

#### IMP-09: Stability Verification

* Have you verified the stability of the inference model?
	+ Yes / No
* Are verification cases addressing anticipated perturbations in the operational phase due to fluctuations in data input (e.g., noise on sensors) included?
	+ Yes / No
* Are nominal, singular point, edge, and corner cases included in the stability verification?
	+ Yes / No

#### IMP-10: Robustness Verification

* Have you verified the robustness of the inference model in adverse conditions?
	+ Yes / No
* Are test cases including edge or corner cases within the ODD (e.g., weather conditions like snow, fog) and OoD test cases included?
	+ Yes / No

### Inference Model Integration

#### IMP-11: Requirements-Based Verification

* Have you performed requirements-based verification of the inference model behavior when integrated into the AI/ML constituent?
	+ Yes / No