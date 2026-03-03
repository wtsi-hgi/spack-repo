# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicromacromultilevel(RPackage):
	"""Micro-Macro Multilevel Modeling

	Most multilevel methodologies can only model macro-micro
    multilevel situations in an unbiased way, wherein group-level predictors
    (e.g., city temperature) are used to predict an individual-level
    outcome variable (e.g., citizen personality). In contrast,
    this R package enables researchers to model micro-macro situations, wherein
    individual-level (micro) predictors (and other group-level predictors) are
    used to predict a group-level (macro) outcome variable in an unbiased way.
	"""
	
	cran = "MicroMacroMultilevel" 

	version("0.4.0", md5="5f0d9265b7241c04e898379dbdfbe4ea")

	depends_on("r@3.1:", type=("build", "run"))
