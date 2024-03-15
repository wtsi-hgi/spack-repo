# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpsftm(RPackage):
	"""Rank Preserving Structural Failure Time Models

	Implements methods described by the paper Robins and Tsiatis (1991) <DOI:10.1080/03610929108830654>. These use g-estimation to estimate the causal effect of a treatment in a two-armed randomised control trial where non-compliance exists and is measured, under an assumption of an accelerated failure time model and no unmeasured confounders.
	"""
	
	cran = "rpsftm" 

	version("1.2.9", md5="2adb2546e506eba7cb63d15792bbd80d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
