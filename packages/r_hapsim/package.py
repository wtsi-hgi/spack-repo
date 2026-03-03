# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapsim(RPackage):
	"""Haplotype Data Simulation

	Package for haplotype-based genotype simulations. Haplotypes are
        generated such that their allele frequencies and linkage
        disequilibrium coefficients match those estimated from an input
        data set.
	"""
	
	cran = "hapsim" 

	version("0.31", md5="d7ae6bbdbcc3196f600ca0d8ca1dfc8f")

	depends_on("r-mass", type=("build", "run"))
