# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepgbm(RPackage):
	"""Stepwise Variable Selection for Generalized Boosted Regression
Modeling

	An introduction to a couple of novel predictive variable selection methods for generalised boosted regression modeling (gbm). They are based on various variable influence methods (i.e., relative variable influence (RVI) and knowledge informed RVI (i.e., KIRVI, and KIRVI2)) that adopted similar ideas as AVI, KIAVI and KIAVI2 in the 'steprf' package, and also based on predictive accuracy in stepwise algorithms. For details of the variable selection methods, please see: Li, J., Siwabessy, J., Huang, Z. and Nichol, S. (2019) <doi:10.3390/geosciences9040180>. Li, J., Alvarez, B., Siwabessy, J., Tran, M., Huang, Z., Przeslawski, R., Radke, L., Howard, F., Nichol, S. (2017). <DOI: 10.13140/RG.2.2.27686.22085>.
	"""
	
	cran = "stepgbm" 

	version("1.0.1", md5="a2d63fbb93e5036f2e31a49aec91727a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spm", type=("build", "run"))
	depends_on("r-steprf", type=("build", "run"))
