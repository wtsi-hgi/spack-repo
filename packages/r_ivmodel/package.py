# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvmodel(RPackage):
	"""Statistical Inference and Sensitivity Analysis for Instrumental
Variables Model

	Carries out instrumental variable
    estimation of causal effects, including power analysis, sensitivity analysis,
    and diagnostics. See Kang, Jiang, Zhao, and Small (2020) <http://pages.cs.wisc.edu/~hyunseung/> for details.
	"""
	
	cran = "ivmodel" 

	version("1.9.1", md5="51c899ea30eec09a5c396df209c5b350")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
