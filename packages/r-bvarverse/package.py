# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvarverse(RPackage):
	"""Tidy Bayesian Vector Autoregression

	Functions to prepare tidy objects from estimated models via 'BVAR'
    (see Kuschnig & Vashold, 2019 <doi:10.13140/RG.2.2.25541.60643>) and
    visualisation thereof. Bridges the gap between estimating models with 'BVAR'
    and plotting the results in a more sophisticated way with 'ggplot2' as well
    as passing them on in a tidy format. 
	"""
	
	homepage = "https://github.com/nk027/bvarverse"
	cran = "BVARverse" 

	version("0.0.1", md5="ca2b88fe7a2c28003a311eb51a94c25d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bvar", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
