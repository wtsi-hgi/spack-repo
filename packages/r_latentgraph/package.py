# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatentgraph(RPackage):
	"""Graphical Models with Latent Variables

	Three methods are provided to estimate graphical models with latent variables: (1) Jin, Y., Ning, Y., and Tan, K. M. (2020) (preprint available); (2) Chandrasekaran, V., Parrilo, P. A. & Willsky, A. S. (2012) <doi:10.1214/11-AOS949>; (3) Tan, K. M., Ning, Y., Witten, D. M. & Liu, H. (2016) <doi:10.1093/biomet/asw050>.
	"""
	
	cran = "latentgraph" 

	version("1.1", md5="9c6f900b66b85503ce31b44b069382b1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
