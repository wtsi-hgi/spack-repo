# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHjam(RPackage):
	"""Hierarchical Joint Analysis of Marginal Summary Statistics

	Provides functions to implement a hierarchical approach which is designed to perform joint analysis of summary statistics using the framework of Mendelian Randomization or transcriptome analysis. Reference: Lai Jiang, Shujing Xu, Nicholas Mancuso, Paul J. Newcombe, David V. Conti (2020). "A Hierarchical Approach Using Marginal Summary Statistics for Multiple Intermediates in a Mendelian Randomization or Transcriptome Analysis." <bioRxiv><doi:10.1101/2020.02.03.924241>.
	"""
	
	homepage = "https://github.com/lailylajiang/hJAM"
	cran = "hJAM" 

	version("1.0.0", md5="1982b77821e855c3f2788c33fe6851df")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
