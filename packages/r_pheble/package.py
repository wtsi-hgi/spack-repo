# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPheble(RPackage):
	"""Classifying High-Dimensional Phenotypes with Ensemble Learning

	A system for binary and multi-class classification of
    high-dimensional phenotypic data using ensemble learning. By combining
    predictions from different classification models, this package attempts
    to improve performance over individual learners. The pre-processing,
    training, validation, and testing are performed end-to-end to minimize
    user input and simplify the process of classification.
	"""
	
	cran = "pheble" 

	version("0.1.0", md5="2e40722d73f3a444c0be945e5df16268")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-adabag", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-evtree", type=("build", "run"))
	depends_on("r-frbs", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-hda", type=("build", "run"))
	depends_on("r-hdclassif", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-klar", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpartscore", type=("build", "run"))
	depends_on("r-sparselda", type=("build", "run"))
	depends_on("r-themis", type=("build", "run"))
