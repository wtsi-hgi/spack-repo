# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpready(RPackage):
	"""Preparing Genotypic Datasets in Order to Run Genomic Analysis

	Three functions to clean, summarize and prepare genomic datasets to Genome
    Selection and Genome Association analysis and to estimate population genetic parameters.
	"""
	
	cran = "snpReady" 

	version("0.9.6", md5="b0429b95533ffc81cd593fb48608f976")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
