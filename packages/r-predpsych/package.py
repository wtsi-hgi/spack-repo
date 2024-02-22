# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredpsych(RPackage):
	"""Predictive Approaches in Psychology

	
    Recent years have seen an increased interest in novel methods
    for analyzing quantitative data from experimental psychology. Currently, however, they lack an
    established and accessible software framework. Many existing implementations provide no guidelines,
    consisting of small code snippets, or sets of packages. In addition, the use of existing packages
    often requires advanced programming experience. 'PredPsych' is a user-friendly toolbox based on
    machine learning predictive algorithms. It comprises of multiple functionalities for multivariate
    analyses of quantitative behavioral data based on machine learning models.
	"""
	
	cran = "PredPsych" 

	version("0.4", md5="09b609f02e11424a7a069690f52485a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
