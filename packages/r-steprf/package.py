# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteprf(RPackage):
	"""Stepwise Predictive Variable Selection for Random Forest

	An introduction to several novel predictive variable selection methods for random forest. They are based on various variable importance methods (i.e., averaged variable importance (AVI), and knowledge informed AVI (i.e., KIAVI, and KIAVI2)) and predictive accuracy in stepwise algorithms. For details of the variable selection methods, please see: Li, J., Siwabessy, J., Huang, Z. and Nichol, S. (2019) <doi:10.3390/geosciences9040180>. Li, J., Alvarez, B., Siwabessy, J., Tran, M., Huang, Z., Przeslawski, R., Radke, L., Howard, F., Nichol, S. (2017). <DOI: 10.13140/RG.2.2.27686.22085>.
	"""
	
	cran = "steprf" 

	version("1.0.2", md5="816ba55753a34e383b046ea1827128ac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-spm2", type=("build", "run"))
	depends_on("r-psy", type=("build", "run"))
