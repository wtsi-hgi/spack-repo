# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNegativecontroloutcomeadjustment(RPackage):
	"""Estimation of Vaccine Efficacy using Negative Control Outcomes

	Methods to reduce confounding bias from unmeasured confounders in observational studies of vaccine efficacy using negative control outcomes.
	"""
	
	cran = "NegativeControlOutcomeAdjustment" 

	version("0.0.6", md5="c72aa5b055b31e5932cc03effdbe23d9")

	depends_on("r@3.5:", type=("build", "run"))
