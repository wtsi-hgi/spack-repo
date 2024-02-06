# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecoupler(RPackage):
	"""decoupleR: Ensemble of computational methods to infer biological activities from omics data

	Many methods allow us to extract biological activities from omics data using information from prior knowledge resources, reducing the dimensionality for increased statistical power and better interpretability. Here, we present decoupleR, a Bioconductor package containing different statistical methods to extract these signatures within a unified framework. decoupleR allows the user to flexibly test any method with any resource. It incorporates methods that take into account the sign and weight of network interactions. decoupleR can be used with any omic, as long as its features can be linked to a biological process based on prior knowledge. For example, in transcriptomics gene sets regulated by a transcription factor, or in phospho-proteomics phosphosites that are targeted by a kinase.
	"""
	
	homepage = "https://saezlab.github.io/decoupleR/"
	bioc = "decoupleR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/decoupleR_2.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/decoupleR/decoupleR_2.8.0.tar.gz"]

	version("2.8.0", md5="de2a391693476223ec54521aa77ba121")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
