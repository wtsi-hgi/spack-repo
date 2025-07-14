# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidybulk(RPackage):
	"""Brings transcriptomics to the tidyverse

	This is a collection of utility functions that allow to perform exploration of and calculations to RNA sequencing data, in a modular, pipe-friendly and tidy fashion.
	"""
	
	homepage = "https://github.com/stemangiola/tidybulk"
	bioc = "tidybulk"

	version("1.20.0", commit="101515a42cb5b13a9a94158aee1460679e6cff09")
	version("1.14.3", commit="8e3cb1dd76293038bffdc539ff7823be8b0b5eb7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ttservice@0.3.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
