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

	version("1.14.0", commit="7b066896d609d8335e349830b4dac44a87f2ea8b")
	version("1.8.0", commit="3af59000b3ec00485bfdc3280aeb5a99940f12a7")

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
