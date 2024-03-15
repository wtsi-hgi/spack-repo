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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/microbiomeDataSets_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/microbiomeDataSets/microbiomeDataSets_1.10.0.tar.gz"]

	version("1.10.0", md5="90cd4bb36dafcef8f6eb0e0232afdcd0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))

	# experiment