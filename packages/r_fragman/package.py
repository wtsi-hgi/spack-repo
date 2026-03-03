# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFragman(RPackage):
	"""Fragment Analysis in R

	Performs fragment analysis using genetic data coming from capillary electrophoresis machines. These are files with FSA extension which stands for FASTA-type file, and .txt files from Beckman CEQ 8000 system, both contain DNA fragment intensities read by machinery. In addition to visualization, it performs automatic scoring of SSRs (Sample Sequence Repeats; a type of genetic marker very common across the genome) and other type of PCR markers (standing for Polymerase Chain Reaction) in biparental populations such as F1, F2, BC (backcross), and diversity panels (collection of genetic diversity).
	"""
	
	homepage = "http://www.wisc.edu"
	cran = "Fragman" 

	version("1.0.9", md5="0ab66230f2b85b9ca30cdb6cb3d36063")

	depends_on("r@2.10:", type=("build", "run"))
