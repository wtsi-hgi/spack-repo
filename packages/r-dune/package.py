# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDune(RPackage):
	"""Improving replicability in single-cell RNA-Seq cell type discovery

	Given a set of clustering labels, Dune merges pairs of clusters to increase mean ARI between labels, improving replicability.
	"""
	
	bioc = "Dune" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Dune_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Dune/Dune_1.14.0.tar.gz"]

	version("1.14.0", md5="afc7d133de0af7ccdc64a9a7a3722ccb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
