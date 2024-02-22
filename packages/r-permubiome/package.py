# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermubiome(RPackage):
	"""A Permutation Based Test for Biomarker Discovery in Microbiome
Data

	The permubiome R package was created to perform a permutation-based non-parametric analysis on microbiome data for biomarker discovery aims. This test executes thousands of comparisons in a pairwise manner, after a random shuffling of data into the different groups of study with a prior selection of the microbiome features with the largest variation among groups. Previous to the permutation test itself, data can be normalized according to different methods proposed to handle microbiome data ('proportions' or 'Anders'). The median-based differences between groups resulting from the multiple simulations are fitted to a normal distribution with the aim to calculate their significance. A multiple testing correction based on Benjamini-Hochberg method (fdr) is finally applied to extract the differentially presented features between groups of your dataset. LATEST UPDATES: v1.1 and olders incorporates function to parse COLUMN format; v1.2 and olders incorporates -optimize- function to maximize evaluation of features with largest inter-class variation; v1.3 and olders includes the -size.effect- function to perform estimation statistics using the bootstrap-coupled approach implemented in the 'dabestr' (>=0.3.0) R package. Current v1.3.2 fixed bug with "Class" recognition and updated 'dabestr' functions.
	"""
	
	cran = "permubiome" 

	version("1.3.2", md5="88511d4614f1f11b8872293bdac3a785")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dabestr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
