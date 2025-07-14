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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Dune_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Dune/Dune_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="0485adfe2acd245824e1c7eaa356338cbecdad24fa53585b29b46ab4b5b914cc")

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
