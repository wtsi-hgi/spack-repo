# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskpredictclustdata(RPackage):
	"""Assessing Risk Predictions for Clustered Data

	Assessing and comparing risk prediction rules for clustered data. The method is based on the paper: Rosner B, Qiu W, and Lee MLT.(2013) <doi: 10.1007/s10985-012-9240-6>.
	"""
	
	cran = "riskPredictClustData" 

	version("0.2.6", md5="4c81e1b1583cec5501bf313b7014ea91")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
