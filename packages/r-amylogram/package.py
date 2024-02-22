# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmylogram(RPackage):
	"""Prediction of Amyloid Proteins

	Predicts amyloid proteins using random forests trained on the
    n-gram encoded peptides. The implemented algorithm can be accessed from
    both the command line and shiny-based GUI.
	"""
	
	homepage = "https://github.com/michbur/AmyloGram"
	cran = "AmyloGram" 

	version("1.1", md5="e0759212c89f5af7897c195136bfdeac")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biogram", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
