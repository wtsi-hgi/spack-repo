# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstarm(RPackage):
	"""Analyze Two Choice Reaction Time Data with the D*M Method

	A collection of functions to estimate parameters of a diffusion model via a D*M analysis. Build in models are: the Ratcliff diffusion model, the RWiener diffusion model, and Linear Ballistic Accumulator models. Custom models functions can be specified as long as they have a density function.
	"""
	
	homepage = "https://github.com/vandenman/DstarM"
	cran = "DstarM" 

	version("0.4.0", md5="aa663f36c4513e0f82824bc5ab671d4f")

	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-rwiener", type=("build", "run"))
	depends_on("r-rtdists", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
