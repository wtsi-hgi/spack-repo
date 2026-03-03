# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwde(RPackage):
	"""Models and Tests for Departure from Hardy-Weinberg Equilibrium
and Independence Between Loci

	Fits models for genotypic disequilibria, as described in
  Huttley and Wilson (2000) <doi:10.1093/genetics/156.4.2127>, Weir (1996) and Weir and Wilson (1986).
  Contrast terms are available that account for first order interactions
  between loci.  Also implements, for a single locus in a single
  population, a conditional exact test for Hardy-Weinberg equilibrium.
	"""
	
	homepage = "https://github.com/jhmaindonald/hwde"
	cran = "hwde" 

	version("0.67-3", md5="37182624369effed2117de2a39c0db3c")

	depends_on("r@2:", type=("build", "run"))
