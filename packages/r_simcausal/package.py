# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcausal(RPackage):
	"""Simulating Longitudinal Data with Causal Inference Applications

	A flexible tool for simulating complex longitudinal data using
    structural equations, with emphasis on problems in causal inference.
    Specify interventions and simulate from intervened data generating
    distributions. Define and evaluate treatment-specific means, the average
    treatment effects and coefficients from working marginal structural models.
    User interface designed to facilitate the conduct of transparent and
    reproducible simulation studies, and allows concise expression of complex
    functional dependencies for a large number of time-varying nodes. See the
    package vignette for more information, documentation and examples.
	"""
	
	homepage = "https://github.com/osofr/simcausal"
	cran = "simcausal" 

	version("0.5.6", md5="2fcf4bc78c0fb8756ba087d0c53a8386")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
