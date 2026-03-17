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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/decoupleR_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/decoupleR/decoupleR_2.8.0.tar.gz"]


	version(
        "2.9.7",
        sha256="a4adc855862b31268fbff9f7a3e5e13ec9ad416cc17dd43a5d72c46492fddb5d",
        url="https://github.com/saezlab/decoupleR/archive/refs/tags/v2.9.7.tar.gz",
    )
	version(
        "2.9.6",
        sha256="64af52a6e1a8127e81421ceb3cb680e9680a3d81c3fae8e4140f314e27588044",
        url="https://github.com/saezlab/decoupleR/archive/refs/tags/v2.9.6.tar.gz",
    )
	version(
        "2.9.5",
        sha256="9ee0de14c49acad129db097e6f5944b21083dfd42e4fafdcee3226fbf16abb96",
        url="https://github.com/saezlab/decoupleR/archive/refs/tags/v2.9.5.tar.gz",
    )
	version(
        "2.9.4",
        sha256="0333cb8f4b4a39dc81a2b721d02d7d1a1d28a6bb681a214350c4d1c4c4d51dfa",
        url="https://github.com/saezlab/decoupleR/archive/refs/tags/v2.9.4.tar.gz",
    )
	version("2.8.0", md5="de2a391693476223ec54521aa77ba121")


	with default_args(type=("build", "run")): 
		depends_on("r@4:")

		with when("@2.9:"):
			depends_on("r-biocparallel")
			depends_on("r-parallelly")

		depends_on("r-broom")
		depends_on("r-dplyr")
		depends_on("r-magrittr")
		depends_on("r-matrix")
		depends_on("r-purrr")
		depends_on("r-rlang")
		depends_on("r-stringr")
		depends_on("r-tibble")
		depends_on("r-tidyr")
		depends_on("r-tidyselect")
		depends_on("r-withr")
