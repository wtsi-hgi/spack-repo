# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBearscc(RPackage):
	"""BEARscc (Bayesian ERCC Assesstment of Robustness of Single Cell Clusters)

	BEARscc is a noise estimation and injection tool that is designed to assess putative single-cell RNA-seq clusters in the context of experimental noise estimated by ERCC spike-in controls.
	"""
	
	bioc = "BEARscc"

	version("1.28.0", commit="070291e94f8f5f9e4a81a9b9310a80b1b7544c5d")
	version("1.22.0", commit="243e1c2f2ec9b9d3e9e9e279c0a5da9ee4a40fb0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
