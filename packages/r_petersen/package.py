# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPetersen(RPackage):
	"""Estimators for Two-Sample Capture-Recapture Studies

	A comprehensive implementation of Petersen-type estimators
    and its many variants for two-sample capture-recapture studies.
    A conditional likelihood approach is used that allows
    for tag loss; non reporting of tags; reward tags; categorical, geographical and temporal stratification;
    partial stratification; reverse capture-recapture;
    and continuous variables in modeling the probability of capture.
    Many examples from fisheries management are presented.
	"""
	
	homepage = "https://github.com/cschwarz-stat-sfu-ca/Petersen"
	cran = "Petersen" 

	version("2023.12.1", md5="fadca07c7882c525d8734bcb43d285bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-btspas", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-spas", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
