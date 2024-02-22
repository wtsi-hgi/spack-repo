# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGorica(RPackage):
	"""Evaluation of Inequality Constrained Hypotheses Using GORICA

	Implements the generalized order-restricted information criterion
    approximation (GORICA), an AIC-like information criterion that can be
    utilized to evaluate informative hypotheses specifying directional
    relationships between model parameters in terms of (in)equality
    constraints (see Altinisik, Van Lissa, Hoijtink, Oldehinkel, & Kuiper,
    2021), <doi:10.31234/osf.io/t3c8g>. The GORICA is applicable not only to
    normal linear models, but also to generalized linear models (GLMs), 
    generalized linear mixed models (GLMMs), structural equation models
    (SEMs), and contingency tables. For contingency tables, restrictions on cell
    probabilities can be non-linear.
	"""
	
	homepage = "https://informative-hypotheses.sites.uu.nl/software/goric/"
	cran = "gorica" 

	version("0.1.4", md5="93a399a3bbc0184e5a5115efadd4b0f4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bain@0.2.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
