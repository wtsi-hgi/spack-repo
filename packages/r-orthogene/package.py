# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthogene(RPackage):
	"""Interspecies gene mapping

	`orthogene` is an R package for easy mapping of orthologous genes across hundreds of species. It pulls up-to-date gene ortholog mappings across **700+ organisms**. It also provides various utility functions to aggregate/expand common objects (e.g. data.frames, gene expression matrices, lists) using **1:1**, **many:1**, **1:many** or **many:many** gene mappings, both within- and between-species.
	"""
	
	homepage = "https://github.com/neurogenomics/orthogene"
	bioc = "orthogene" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/orthogene_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/orthogene/orthogene_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="2872b0c24173b02dca976253f58310fe26bd5f3ad4bae2e02be19914405b824f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-homologene", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-babelgene", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-grr", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
