# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomedatasets(RPackage):
	"""Experiment Hub based microbiome datasets

	microbiomeDataSets is a collection of microbiome datasets loaded from Bioconductor'S ExperimentHub infrastructure. The datasets serve as reference for workflows and vignettes published adjacent to the microbiome analysis tools on Bioconductor. Additional datasets can be added overtime and additions from authors are welcome.
	"""
	
	bioc = "microbiomeDataSets"

	version("1.16.0", commit="5c73287cf4c40638db06eb588ad4bb8112266e1a")
	version("1.10.0", commit="d02a75a50583e539f05dd34c8128cf456b8b5744")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))

