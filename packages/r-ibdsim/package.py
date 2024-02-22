# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbdsim(RPackage):
	"""Simulation of Chromosomal Regions Shared by Family Members

	Simulation of segments shared identical-by-descent (IBD) by 
    pedigree members. Using sex specific recombination rates along the human
    genome (Kong et. al (2010) <doi:10.1038/nature09525>), phased chromosomes
    are simulated for all pedigree members, either by unconditional gene 
    dropping or conditional on a specified IBD pattern. Additional functions 
    provide summaries and further analysis of the simulated genomes.
	"""
	
	cran = "IBDsim" 

	version("0.9-8", md5="e8fd06b9868477235deb67858d1e41a7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-paramlink@1.1:", type=("build", "run"))
