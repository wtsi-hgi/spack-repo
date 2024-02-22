# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTramnet(RPackage):
	"""Penalized Transformation Models

	Partially penalized versions of specific transformation models
    implemented in package 'mlt'. Available models include a fully parametric version
    of the Cox model, other parametric survival models (Weibull, etc.), models for
    binary and ordered categorical variables, normal and transformed-normal (Box-Cox type)
    linear models, and continuous outcome logistic regression. Hyperparameter tuning
    is facilitated through model-based optimization functionalities from package 'mlrMBO'.
    The accompanying vignette describes the methodology used in 'tramnet' in detail.
    Transformation models and model-based optimization are described in
    Hothorn et al. (2019) <doi:10.1111/sjos.12291> and
    Bischl et al. (2016) <arxiv:1703.03373>, respectively.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "tramnet" 

	version("0.0-8", md5="51d31fda93afbb493a1f9906bac5d4de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tram@0.3.2:", type=("build", "run"))
	depends_on("r-cvxr@0.99.4:", type=("build", "run"))
	depends_on("r-mlrmbo@1.1.2:", type=("build", "run"))
	depends_on("r-mlt", type=("build", "run"))
	depends_on("r-basefun", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-paramhelpers", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-smoof", type=("build", "run"))
