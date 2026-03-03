# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmise(RPackage):
	"""A General Framework of Multivariate Mixed-Effects Selection
Models

	Offers a general framework of multivariate mixed-effects
        models for the joint analysis of multiple correlated outcomes with clustered 
        data structures and potential missingness proposed by Wang et al. (2018) <doi:10.1093/biostatistics/kxy022>. The missingness of outcome values may 
        depend on the values themselves (missing not at random and non-ignorable), 
        or may depend on only the covariates (missing at random and ignorable), or both.
        This package provides functions for two models: 1) mvMISE_b() 
        allows correlated outcome-specific random intercepts with a factor-analytic 
        structure, and 2) mvMISE_e() allows the correlated outcome-specific 
        error terms with a graphical lasso penalty on the error precision matrix. Both functions 
        are motivated by the multivariate data analysis on data with clustered structures 
        from labelling-based quantitative proteomic studies. These models and functions 
        can also be applied to univariate and multivariate analyses of clustered data 
        with balanced or unbalanced design and no missingness.
	"""
	
	homepage = "https://github.com/randel/mvMISE"
	cran = "mvMISE" 

	version("1.0", md5="37c3ff197573d417dd3ea5d8deb8004b")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
