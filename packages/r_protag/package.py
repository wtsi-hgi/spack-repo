# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtag(RPackage):
	"""Search Tagged Peptides & Draw Highlighted Mass Spectra

	In a typical protein labelling procedure, proteins are chemically tagged with a functional group, usually at specific sites, then digested into peptides, which are then analyzed using matrix-assisted laser desorption ionization - time of flight mass spectrometry (MALDI-TOF MS) to generate peptide fingerprint. Relative to the control, peptides that are heavier by the mass of the labelling group are informative for sequence determination. Searching for peptides with such mass shifts, however, can be difficult. This package, designed to tackle this inconvenience, takes as input the mass list of two or multiple MALDI-TOF MS mass lists, and makes pairwise comparisons between the labeled groups vs. control, and restores centroid mass spectra with highlighted peaks of interest for easier visual examination. Particularly, peaks differentiated by the mass of the labelling group are defined as a “pair”, those with equal masses as a “match”, and all the other peaks as a “mismatch”.For more bioanalytical background information, refer to following publications: Jingjing Deng (2015) <doi:10.1007/978-1-4939-2550-6_19>; Elizabeth Chang (2016) <doi:10.7171/jbt.16-2702-002>.
	"""
	
	cran = "protag" 

	version("1.0.0", md5="f14d38c51b68d9766cf7f7344cf653b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
