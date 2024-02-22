# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamabiomd(RPackage):
	"""Diversity Analysis for Sequence Data

	The full form is Garai and Mantri Biological Material Diversity. It is an R package designed for the calculation of biological diversity using sequence data. It simplifies the process by requiring only sample IDs and accession numbers. Whether you're analyzing genetic or microbial diversity, It provides efficient tools for diversity analysis. Serially one should go for the functions as presented here expand_accession_ranges(), get_sequence_information(), preprocess_for_alignment(), write_fasta(), SampleID_vs_NumSequences(), data_sampling(), alignment_info(), compute_average_similarity_matrix(), generate_heatmaps(), clustering_average_similarity(), clustering_percent_similarity(), bubble_plot_count(), bubble_plot_percentage(), tree_average_similarity(), tree_percent_similarity(). Till date there are total 15 functions. More details can be found in Faith (1992) <doi:10.1016/0006-3207(92)91201-3>.
	"""
	
	cran = "GaMaBioMD" 

	version("0.2.0", md5="8b27e1bce2da2c6c2e05522cfa6e9935")

	depends_on("r-traits", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
