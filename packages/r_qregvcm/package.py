# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQregvcm(RPackage):
	"""Quantile Regression in Varying-Coefficient Models

	Quantile regression in varying-coefficient models (VCM) using one particular nonparametric technique called P-splines. The functions can be applied on three types of VCM; (1) Homoscedastic VCM, (2) Simple heteroscedastic VCM, and (3) General heteroscedastic VCM. 
	"""
	
	cran = "QRegVCM" 

	version("1.2", md5="d4f583a4c6da307ea4f1fc093bf3b3f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-truncsp", type=("build", "run"))
