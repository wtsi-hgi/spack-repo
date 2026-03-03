# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectr(RPackage):
	"""Predicts Oomycete Effectors

	Predicts cytoplasmic effector proteins using genomic data by searching for motifs of interest using regular expression searches and hidden Markov models (HMM) based in Haas et al. (2009) <doi:10.1038/nature08358>. 
	"""
	
	cran = "effectR" 

	version("1.0.2", md5="08dbce84b129497d4bb54f5fa8789ac2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-seqinr@3.3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
