# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlemi(RPackage):
	"""Statistical Learning Based Estimation of Mutual Information

	The implementation of the algorithm for estimation of mutual information and channel capacity from experimental data by classification procedures (logistic regression). Technically, it allows to estimate information-theoretic measures between finite-state input and multivariate, continuous output. Method described in Jetka et al. (2019) <doi:10.1371/journal.pcbi.1007132>.
	"""
	
	homepage = "https://github.com/TJetka/SLEMI"
	cran = "SLEMI" 

	version("1.0.2", md5="2cda258ef3b24216d55aaa788898a740")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
