# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGscramble(RPackage):
	"""Simulating Admixed Genotypes Without Replacement

	A genomic simulation approach for creating biologically
    informed individual genotypes from empirical data that 1) samples alleles
    from populations without replacement, 2) segregates alleles based on species-specific
    recombination rates. 'gscramble' is a flexible simulation approach that allows users
    to create pedigrees of varying complexity in order to simulate admixed genotypes.
    Furthermore, it allows users to track haplotype blocks from the source populations
    through the pedigrees.
	"""
	
	homepage = "https://github.com/eriqande/gscramble"
	cran = "gscramble" 

	version("1.0.1", md5="33d872ef340a0dbcad8c31c23f245a0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
