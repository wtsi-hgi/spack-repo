# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeme(RPackage):
	"""Small Area Estimation with Measurement Error

	A set of functions and datasets implementation of small area estimation when auxiliary variable is measured with error. These functions provide a empirical best linear unbiased prediction (EBLUP) estimator and mean squared error (MSE) estimator of the EBLUP. These models were developed by Ybarra and Lohr (2008) <doi:10.1093/biomet/asn048>.
	"""
	
	cran = "saeME" 

	version("1.3.1", md5="1d940009a5e2f599375e19afee1e48b4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
