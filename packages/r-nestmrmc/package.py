# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestmrmc(RPackage):
	"""Single Reader Between-Cases AUC Estimator in Nested Data

	This R package provides a calculation of between-cases AUC estimate, corresponding covariance, and variance estimate in the nested data problem.  Also, the package has the function to simulate the nested data. The calculated between-cases AUC estimate is used to evaluate the reader's diagnostic performance in clinical tasks with nested data. For more details on the above methods, please refer to the paper by H Du, S Wen, Y Guo, F Jin, BD Gallas (2022) <doi:10.1177/09622802221111539>. 
	"""
	
	cran = "NestMRMC" 

	version("1.0", md5="0bce06eb6657d35f066e3204695ac622")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-imrmc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
