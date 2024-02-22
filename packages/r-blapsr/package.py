# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlapsr(RPackage):
	"""Bayesian Inference with Laplace Approximations and P-Splines

	Laplace approximations and penalized B-splines are combined
    for fast Bayesian inference in latent Gaussian models. The routines can be
    used to fit survival models, especially proportional hazards and promotion 
    time cure models (Gressani, O. and Lambert, P. (2018) 
    <doi:10.1016/j.csda.2018.02.007>). The Laplace-P-spline methodology can also
    be implemented for inference in (generalized) additive models
    (Gressani, O. and Lambert, P. (2021) <doi:10.1016/j.csda.2020.107088>).
    See the associated website for more information and examples.
	"""
	
	homepage = "<https://www.blapsr-project.org/>"
	cran = "blapsr" 

	version("0.6.1", md5="b65c7bb7705092a094008482a4190218")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival@2.44.1:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-mass@7.3.51:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-rspectra@0.16:", type=("build", "run"))
	depends_on("r-sn@1.5.4:", type=("build", "run"))
