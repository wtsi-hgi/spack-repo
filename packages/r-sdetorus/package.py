# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdetorus(RPackage):
	"""Statistical Tools for Toroidal Diffusions

	Implementation of statistical methods for the estimation of
    toroidal diffusions. Several diffusive models are provided, most of them
    belonging to the Langevin family of diffusions on the torus. Specifically,
    the wrapped normal and von Mises processes are included, which can be seen
    as toroidal analogues of the Ornstein-Uhlenbeck diffusion. A collection of
    methods for approximate maximum likelihood estimation, organized in four
    blocks, is given: (i) based on the exact transition probability density,
    obtained as the numerical solution to the Fokker-Plank equation; (ii) based
    on wrapped pseudo-likelihoods; (iii) based on specific analytic
    approximations by wrapped processes; (iv) based on maximum likelihood of
    the stationary densities. The package allows the replicability of the
    results in García-Portugués et al. (2019) <doi:10.1007/s11222-017-9790-2>.
	"""
	
	homepage = "https://github.com/egarpor/sdetorus"
	cran = "sdetorus" 

	version("0.1.9", md5="7cd904332fe8d90aa80cf6c2d11facf5")
	version("0.1.10", md5="fcdc8e53da04d8d951b05b95a9001fe2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
