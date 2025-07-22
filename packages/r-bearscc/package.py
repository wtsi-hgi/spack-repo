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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BEARscc_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BEARscc/BEARscc_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="68ff48d568b37593cb77ff6694ba6b4a6fae51ee96747c2bf4bbcd6db1abb653")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
