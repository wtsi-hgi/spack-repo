# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoscore(RPackage):
	"""An Interpretable Machine Learning-Based Automatic Clinical Score
Generator

	A novel interpretable machine learning-based framework to automate the development of a clinical scoring model for predefined outcomes. Our novel framework consists of six modules: variable ranking with machine learning, variable transformation, score derivation, model selection, domain knowledge-based score fine-tuning, and performance evaluation.The The original AutoScore structure is described in the research paper<doi:10.2196/21798>. A full tutorial can be found here<https://nliulab.github.io/AutoScore/>. Users or clinicians could seamlessly generate parsimonious sparse-score risk models (i.e., risk scores), which can be easily implemented and validated in clinical practice. We hope to see its application in various medical case studies.
	"""
	
	homepage = "https://github.com/nliulab/AutoScore"
	cran = "AutoScore" 

	version("1.0.0", md5="e142760caa43360d8b661cb9d6a1fc8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-coxed", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survauc", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
