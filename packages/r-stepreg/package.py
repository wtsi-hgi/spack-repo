# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepreg(RPackage):
	"""Stepwise Regression Analysis

	Three most common types of stepwise regression including linear regression, logistic regression and cox proportional hazard regression can be performed to select best model with methods of forward selection, backward elimination, bidirectional selection and best subset selection. A widely used selection criteria are available for variable selection.
	"""
	
	cran = "StepReg" 

	version("1.4.4", md5="8c7addbe6ab1eec8e69a955975fdb83b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
