# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTranscriptogramer(RPackage):
	"""Transcriptional analysis based on transcriptograms

	R package for transcriptional analysis based on transcriptograms, a method to analyze transcriptomes that projects expression values on a set of ordered proteins, arranged such that the probability that gene products participate in the same metabolic pathway exponentially decreases with the increase of the distance between two proteins of the ordering. Transcriptograms are, hence, genome wide gene expression profiles that provide a global view for the cellular metabolism, while indicating gene sets whose expressions are altered.
	"""
	
	homepage = "https://github.com/arthurvinx/transcriptogramer"
	bioc = "transcriptogramer"

	version("1.30.0", commit="0f183b214350a0606436c172f78814c30737f146")
	version("1.24.0", commit="f288ab4889aca103db694b203433dcacdf9c5818")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-reder", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
