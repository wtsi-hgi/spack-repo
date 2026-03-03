# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGalamm(RPackage):
	"""Generalized Additive Latent and Mixed Models

	Estimates generalized additive latent and
    mixed models using maximum marginal likelihood, 
    as defined in Sorensen et al. (2023) 
    <doi:10.1007/s11336-023-09910-z>, which is an extension of Rabe-Hesketh and
    Skrondal (2004)'s unifying framework for multilevel latent variable 
    modeling <doi:10.1007/BF02295939>. Efficient computation is done using sparse 
    matrix methods, Laplace approximation, and automatic differentiation. The 
    framework includes generalized multilevel models with heteroscedastic 
    residuals, mixed response types, factor loadings, smoothing splines, 
    crossed random effects, and combinations thereof. Syntax for model 
    formulation is close to 'lme4' (Bates et al. (2015) 
    <doi:10.18637/jss.v067.i01>) and 'PLmixed' (Rockwood and Jeon (2019) 
    <doi:10.1080/00273171.2018.1516541>).
	"""
	
	homepage = "https://github.com/LCBC-UiO/galamm"
	cran = "galamm" 

	version("0.1.1", md5="a4a4cf3fbb24cca2239dfcf33e02a89c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
