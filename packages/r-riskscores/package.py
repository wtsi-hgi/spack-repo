# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskscores(RPackage):
	"""Optimized Integer Risk Score Models

	Implements an optimized approach to learning risk score models, where sparsity and integer constraints are integrated into the model-fitting process.
	"""
	
	homepage = "https://github.com/hjeglinton/riskscores"
	cran = "riskscores" 

	version("1.0.2", md5="dcedcfcb4cb439f136759a498f6377a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
