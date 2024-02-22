# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGldrm(RPackage):
	"""Generalized Linear Density Ratio Models

	Fits a generalized linear density ratio model (GLDRM).
    A GLDRM is a semiparametric generalized linear model.
    In contrast to a GLM, which assumes a particular exponential family distribution, 
    the GLDRM uses a semiparametric likelihood to estimate the reference distribution. 
    The reference distribution may be any discrete, continuous, or mixed exponential 
    family distribution. The model parameters, which include both the regression 
    coefficients and the cdf of the unspecified reference distribution, are estimated 
    by maximizing a semiparametric likelihood. Regression coefficients are estimated 
    with no loss of efficiency, i.e. the asymptotic variance is the same as if the 
    true exponential family distribution were known.
    Huang (2014) <doi:10.1080/01621459.2013.824892>.
    Huang and Rathouz (2012) <doi:10.1093/biomet/asr075>.
    Rathouz and Gao (2008) <doi:10.1093/biostatistics/kxn030>.
	"""
	
	cran = "gldrm" 

	version("1.6", md5="8660519ee3bf69bccd728d17e25689f4")

	depends_on("r@3.2.2:", type=("build", "run"))
