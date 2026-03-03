# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaploStats(RPackage):
	"""Statistical Analysis of Haplotypes with Traits and Covariates
when Linkage Phase is Ambiguous

	Routines for the analysis of indirectly measured haplotypes. The statistical methods assume that all subjects are unrelated and that haplotypes are ambiguous (due to unknown linkage phase of the genetic markers). The main functions are: haplo.em(), haplo.glm(), haplo.score(), and haplo.power(); all of which have detailed examples in the vignette.
	"""
	
	homepage = "https://analytictools.mayo.edu/research/haplo-stats/"
	cran = "haplo.stats" 

	version("1.9.5.1", md5="9b6a3a7ee49829675b42c59ad8f65197")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-arsenal", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
