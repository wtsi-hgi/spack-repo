# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfar(RPackage):
	"""Stochastic Frontier Analysis Routines

	Maximum likelihood estimation for stochastic frontier
    analysis (SFA) of production (profit) and cost functions. The package
    includes the basic stochastic frontier for cross-sectional or pooled
    data with several distributions for the one-sided error term (i.e.,
    Rayleigh, gamma, Weibull, lognormal, uniform, generalized exponential
    and truncated skewed Laplace), the latent class stochastic frontier
    model (LCM) as described in Dakpo et al. (2021)
    <doi:10.1111/1477-9552.12422>, for cross-sectional and pooled data,
    and the sample selection model as described in Greene (2010)
    <doi:10.1007/s11123-009-0159-1>, and applied in Dakpo et al. (2021)
    <doi:10.1111/agec.12683>.  Several possibilities in terms of
    optimization algorithms are proposed.
	"""
	
	homepage = "https://github.com/hdakpo/sfaR"
	cran = "sfaR" 

	version("1.0.0", md5="ebdbfe8afdb2c948299be1b0cc5dea5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-marqlevalg", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mnorm", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-trustoptim", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
