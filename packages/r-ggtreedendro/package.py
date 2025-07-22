# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtreedendro(RPackage):
	"""Drawing 'dendrogram' using 'ggtree'

	Offers a set of 'autoplot' methods to visualize tree-like structures (e.g., hierarchical clustering and classification/regression trees) using 'ggtree'. You can adjust graphical parameters using grammar of graphic syntax and integrate external data to the tree.
	"""
	
	bioc = "ggtreeDendro" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggtreeDendro_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggtreeDendro/ggtreeDendro_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="ace77cc34d998168e516ef377b563d49d9d8895135fdc6cdb9359544f6b2df3e")

	depends_on("r-ggtree@3.5.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidytree", type=("build", "run"))
