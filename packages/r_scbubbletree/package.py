# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbubbletree(RPackage):
	"""Quantitative visual exploration of scRNA-seq data

	scBubbletree is a quantitative method for visual exploration of scRNA-seq data. It preserves biologically meaningful properties of scRNA-seq data, such as local and global cell distances, as well as the density distribution of cells across the sample. scBubbletree is scalable and avoids the overplotting problem, and is able to visualize diverse cell attributes derived from multiomic single-cell experiments. Importantly, Importantly, scBubbletree is easy to use and to integrate with popular approaches for scRNA-seq data analysis.
	"""
	
	homepage = "https://github.com/snaketron/scBubbletree"
	bioc = "scBubbletree" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scBubbletree_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scBubbletree/scBubbletree_1.4.0.tar.gz"]

	version("1.4.0", md5="d64f38622d8aec6ebb23e81231710134")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
