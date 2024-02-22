# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROosse(RPackage):
	"""Out-of-Sample R² with Standard Error Estimation

	Estimates out-of-sample R² through bootstrap or cross-validation as a measure of predictive performance. In addition, a standard error for this point estimate is provided, and confidence intervals are constructed.
	"""
	
	cran = "oosse" 

	version("1.0.11", md5="ca4152a96a5aad0bfec7d3b7fe912998")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
