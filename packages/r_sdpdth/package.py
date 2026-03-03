# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdpdth(RPackage):
	"""M-Estimator for Threshold Spatial Dynamic Panel Data Model

	M-estimator for threshold and non-threshold spatial dynamic panel data model. Yang, Z (2018) <doi:10.1016/j.jeconom.2017.08.019>. Wu, J., Matsuda, Y (2021) <doi:10.1007/s43071-021-00008-1>.
	"""
	
	cran = "sdpdth" 

	version("0.2", md5="9c7e53ab9c03b3a890ca278ecb1e888e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcma", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
