# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectsizescr(RPackage):
	"""Indices for Single-Case Research

	Parametric and nonparametric statistics for single-case design. Regarding nonparametric statistics, the index suggested by Parker, Vannest, Davis and Sauber (2011) <doi:10.1016/j.beth.2010.08.006> was included. It combines both nonoverlap and trend to estimate the effect size of a treatment in a single case design.
	"""
	
	cran = "effectsizescr" 

	version("0.1.0", md5="b4b4b26a9f1254da8cbd6f926545936a")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
