# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvif(RPackage):
	"""Collinearity Detection using Redefined Variance Inflation Factor
and Graphical Methods

	The detection of troubling approximate collinearity in a multiple linear regression model is a classical problem in Econometrics. The objective of this package is to detect it using the variance inflation factor redefined and the scatterplot between the variance inflation factor and the coefficient of variation. For more details see Salmerón R., García C.B. and García J. (2018) <doi:10.1080/00949655.2018.1463376>, Salmerón, R., Rodríguez, A. and García C. (2020) <doi:10.1007/s00180-019-00922-x>, Salmerón, R., García, C.B, Rodríguez, A. and García, C. "Limitations in Detecting Multicollinearity due to Scaling Issues in the mcvis Package" (2022, to appear in The R Journal) and Salmerón, R., García, C.B, García J. (2023, working paper) <arXiv:2005.02245>.
	"""
	
	homepage = "http://colldetreat.r-forge.r-project.org/"
	cran = "rvif" 

	version("1.0", md5="055fa3f6896ca1af9adb7c1bc8976970")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-multicoll", type=("build", "run"))
