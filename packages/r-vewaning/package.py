# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVewaning(RPackage):
	"""Vaccine Efficacy Over Time

	Implements methods for inference on potential waning of vaccine
    efficacy and for estimation of vaccine efficacy at a user-specified time
    after vaccination based on data from a randomized, double-blind,
    placebo-controlled vaccine trial in which participants may be unblinded
    and placebo subjects may be crossed over to the study vaccine.  The
    methods also allow adjustment for possible confounding via inverse
    probability weighting through specification of models for the trial
    entry process, unblinding mechanisms, and the probability an unblinded
    placebo participant accepts study vaccine:  Tsiatis, A. A. and Davidian,
    M. (2021) <arXiv:2102.13103> .
	"""
	
	cran = "VEwaning" 

	version("1.3", md5="a66837feca43dbd82bdd4700e69afe70")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
