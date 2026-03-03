# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrds(RPackage):
	"""Mark-Recapture Distance Sampling

	Animal abundance estimation via conventional, multiple covariate
    and mark-recapture distance sampling (CDS/MCDS/MRDS). Detection function
    fitting is performed via maximum likelihood. Also included are diagnostics
    and plotting for fitted detection functions. Abundance estimation is via a
    Horvitz-Thompson-like estimator.
	"""
	
	homepage = "https://github.com/DistanceDevelopment/mrds/"
	cran = "mrds" 

	version("2.3.0", md5="3153b2fc91d51c908dd697016eecd7d2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-optimx@2013.8.6:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
