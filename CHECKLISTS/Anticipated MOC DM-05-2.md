Here is the checklist generated for the author developing the artificial intelligent - machine learning software and the reviewer reviewing it:

**IDENTITY AND PURPOSE**
=====================

### Author Checklist

* Have I defined the DQRs (Data Quality Requirements) for all data required for training, testing, and verification of the AI/ML constituent?
	+ Is the relevance of the data supported by its intended use?
	+ Can I determine the origin of the data?
	+ Are there requirements related to the annotation process?
	+ Is the format, accuracy, and resolution of the data documented?
	+ Is the traceability of the data from its origin to its final operation through the whole pipeline of operations ensured?
	+ Are mechanisms in place to ensure that the data will not be corrupted while stored, processed, or transmitted over a communication network?
	+ Are the completeness and representativeness of the data sets guaranteed?
	+ Is there independence between the training, validation, and test data sets?

* Have I characterized each type of data representing an operating parameter of the AI/ML constituent ODD?
	+ Accuracy
	+ Resolution
	+ Quality of annotated data
	+ Integrity (assurance that it has not been corrupted while stored, processed, or transmitted)
	+ Necessary manipulations (e.g., anonymization)

### Reviewer Checklist

* Does the author provide clear definitions for DQRs and characterization of each type of data representing an operating parameter of the AI/ML constituent ODD?
	+ Are the relevance of the data supported by its intended use?
	+ Can I determine the origin of the data?
	+ Are there requirements related to the annotation process?
	+ Is the format, accuracy, and resolution of the data documented?
	+ Is the traceability of the data from its origin to its final operation through the whole pipeline of operations ensured?
	+ Are mechanisms in place to ensure that the data will not be corrupted while stored, processed, or transmitted over a communication network?
	+ Are the completeness and representativeness of the data sets guaranteed?
	+ Is there independence between the training, validation, and test data sets?

**CONFIGURATION MANAGEMENT**
=====================

### Author Checklist

* Have I identified configuration items for the AI/ML constituent life-cycle data?
* Am I using versioning, baselining, change control, reproducibility, problem reporting, archiving, and retrieval with retention period for the AI/ML constituent life-cycle data?

### Reviewer Checklist

* Does the author provide clear identification of configuration items for the AI/ML constituent life-cycle data?
* Are all necessary configuration management principles applied to the AI/ML constituent life-cycle data?

**QUALITY AND PROCESS ASSURANCE**
=====================

### Author Checklist

* Have I ensured that quality/process assurance principles are applied to the development of the AI-based system with the required independence level?

### Reviewer Checklist

* Does the author provide evidence that quality/process assurance principles have been applied to the development of the AI-based system with the required independence level?

**REUSE OF AI/ML MODELS**
=====================

### Author Checklist

* Have I considered the replacement or modification of a previously developed AI/ML constituent or ML model?
* Am I considering incorporating already trained ML models (open source models or COTS ML models) in my design of an AI/ML constituent?

### Reviewer Checklist

* Does the author provide justification for reusing ML models and consideration for adapting OD and/or ODD, data quality, change management, explainability, scalability, and other challenges?