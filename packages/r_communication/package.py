# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommunication(RPackage):
	"""Feature Extraction and Model Estimation for Audio of Human
Speech

	Provides fast, easy feature extraction of human speech and model estimation
	     with hidden Markov models. Flexible extraction of phonetic features and their
	     derivatives, with necessary preprocessing options like feature standardization.
	     Communication can estimate supervised and unsupervised hidden Markov models with
	     these features, with cross validation and corrections for auto-correlation in
	     features. Methods developed in Knox and Lucas (2021) <doi:10.7910/DVN.8BTOHQ>.
	"""
	
	cran = "communication" 

	version("0.1", md5="d69c2d21b3034842ac921d0c745c6d40")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-wrassp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.700.2:", type=("build", "run"))
