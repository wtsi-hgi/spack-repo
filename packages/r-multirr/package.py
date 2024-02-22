# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirr(RPackage):
	"""Bias, Precision, and Power for Multi-Level Random Regressions

	Calculates bias, precision, and power for multi-level random regressions. Random regressions are types of hierarchical models in which data are structured in groups and (regression) coefficients can vary by groups. Tools to estimate model performance are designed mostly for scenarios where (regression) coefficients vary at just one level. 'MultiRR' provides simulation and analytical tools (based on 'lme4') to study model performance for random regressions that vary at more than one level (multi-level random regressions), allowing researchers to determine optimal sampling designs.
	"""
	
	cran = "MultiRR" 

	version("1.1", md5="4f582428070d033c05f0337b23081303")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
