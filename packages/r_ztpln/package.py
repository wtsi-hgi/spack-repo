# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZtpln(RPackage):
	"""Zero-Truncated Poisson Lognormal Distribution

	Functions for obtaining the density, random variates
             and maximum likelihood estimates of the Zero-truncated Poisson lognormal
             distribution and their mixture distribution.
	"""
	
	homepage = "https://github.com/mattocci27/ztpln"
	cran = "ztpln" 

	version("0.1.2", md5="e263dae0a997badd7292347a2fb699f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppnumerical@0.3.2:", type=("build", "run"))
