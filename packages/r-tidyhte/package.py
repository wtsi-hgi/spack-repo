# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyhte(RPackage):
	"""Tidy Estimation of Heterogeneous Treatment Effects

	Estimates heterogeneous treatment effects using tidy semantics 
    on experimental or observational data.  Methods are based on the doubly-robust
    learner of Kennedy (n.d.) <arXiv:2004.14497>. You provide a simple
    recipe for what machine learning algorithms to use in estimating the nuisance
    functions and 'tidyhte' will take care of cross-validation, estimation, model
    selection, diagnostics and construction of relevant quantities of interest about
    the variability of treatment effects.
	"""
	
	homepage = "https://github.com/ddimmery/tidyhte"
	cran = "tidyhte" 

	version("1.0.2", md5="b6c5966a31fcbed0b0bd0148b907ee52")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
