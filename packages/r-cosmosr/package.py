# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmosr(RPackage):
	"""COSMOS (Causal Oriented Search of Multi-Omic Space)

	COSMOS (Causal Oriented Search of Multi-Omic Space) is a method that integrates phosphoproteomics, transcriptomics, and metabolomics data sets based on prior knowledge of signaling, metabolic, and gene regulatory networks. It estimated the activities of transcrption factors and kinases and finds a network-level causal reasoning. Thereby, COSMOS provides mechanistic hypotheses for experimental observations across mulit-omics datasets.
	"""
	
	homepage = "https://github.com/saezlab/COSMOSR"
	bioc = "cosmosR"

	version("1.16.0", commit="c5fbdd30a0074cbce5638f96a24dbdf1c3a6dc46")
	version("1.10.0", commit="16a439b56ad81637bf8b12ca2b93a9170fc71e7f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-carnival", type=("build", "run"))
	depends_on("r-dorothea", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-decoupler", type=("build", "run"))
