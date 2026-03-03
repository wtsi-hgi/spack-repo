# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPltesim(RPackage):
	"""Simulate Probabilistic Long-Term Effects in Models with Temporal
Dependence

	Calculates and depicts probabilistic long-term effects
    in binary models with temporal dependence variables. The package performs
    two tasks. First, it calculates the change in the probability of the event
    occurring given a change in a theoretical variable. Second, it calculates
    the rolling difference in the future probability of the event for two
    scenarios: one where the event occurred at a given time and one where the
    event does not occur. The package is consistent with the recent movement to
    depict meaningful and easy-to-interpret quantities of interest with the
    requisite measures of uncertainty. It is the first to make it easy for
    researchers to interpret short- and long-term effects of explanatory
    variables in binary autoregressive models, which can have important
    implications for the correct interpretation of these models.
	"""
	
	homepage = "https://CRAN.R-project.org/package=pltesim"
	cran = "pltesim" 

	version("1.0", md5="8da86c99735ab1b1992eabb952277593")

	depends_on("r-coresim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
