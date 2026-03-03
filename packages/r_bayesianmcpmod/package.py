# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianmcpmod(RPackage):
	"""Simulate, Evaluate, and Analyze Dose Finding Trials with
Bayesian MCPMod

	Bayesian MCPMod (Fleischer et al. (2022) 
    <doi:10.1002/pst.2193>) is an innovative method that improves the
    traditional MCPMod by systematically incorporating historical data,
    such as previous placebo group data. This R package offers functions
    for simulating, analyzing, and evaluating Bayesian MCPMod trials with
    normally distributed endpoints.  It enables the assessment of trial
    designs incorporating historical data across various true
    dose-response relationships and sample sizes. Robust mixture prior
    distributions, such as those derived with the Meta-Analytic-Predictive
    approach (Schmidli et al. (2014) <doi:10.1111/biom.12242>), can be
    specified for each dose group.  Resulting mixture posterior
    distributions are used in the Bayesian Multiple Comparison Procedure
    and modeling steps.  The modeling step also includes a weighted model
    averaging approach (Pinheiro et al. (2014) <doi:10.1002/sim.6052>).
    Estimated dose-response relationships can be bootstrapped and
    visualized.
	"""
	
	homepage = "https://github.com/Boehringer-Ingelheim/BayesianMCPMod"
	cran = "BayesianMCPMod" 

	version("1.0.0", md5="69fa6a2a0911b7d132fc69e3cfb5b703")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dosefinding@1.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rbest", type=("build", "run"))
