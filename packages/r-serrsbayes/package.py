# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerrsbayes(RPackage):
	"""Bayesian Modelling of Raman Spectroscopy

	Sequential Monte Carlo (SMC) algorithms for fitting a generalised additive
    mixed model (GAMM) to surface-enhanced resonance Raman spectroscopy (SERRS),
    using the method of Moores et al. (2016) <arXiv:1604.07299>. Multivariate
    observations of SERRS are highly collinear and lend themselves to a reduced-rank
    representation. The GAMM separates the SERRS signal into three components: a
    sequence of Lorentzian, Gaussian, or pseudo-Voigt peaks; a smoothly-varying baseline;
    and additive white noise. The parameters of each component of the model are estimated
    iteratively using SMC. The posterior distributions of the parameters given the observed
    spectra are represented as a population of weighted particles.
	"""
	
	homepage = "https://github.com/mooresm/serrsBayes"
	cran = "serrsBayes" 

	version("0.5-0", md5="cc7b62d352ada5c5a4ee87673ac5bc38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
