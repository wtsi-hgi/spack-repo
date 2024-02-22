# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmm(RPackage):
	"""Dyadic Mixed Model for Pedigree Data

	Dyadic mixed model analysis with multi-trait responses and
  pedigree-based partitioning of individual variation into a range of
  environmental and genetic variance components for individual and 
  maternal effects. Method documented in dmmOverview.pdf; dmm is an 
  implementation of dispersion mean model described by
  Searle et al. (1992) "Variance Components", Wiley, NY.
	"""
	
	cran = "dmm" 

	version("2.1-9", md5="02935e914f19caa88bf7ff5e08da109a")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
