# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtree(RPackage):
	"""an R package for visualization of tree and annotation data.

	'ggtree' extends the 'ggplot2' plotting system which implemented the
	grammar of graphics. 'ggtree' is designed for visualization and annotation
	of phylogenetic trees and other tree-like structures with their annotation
	data."""

	bioc = "ggtree"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggtree_3.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggtree/ggtree_3.10.1.tar.gz"]

	version("3.10.1", md5="14911b3009b957dcf17ae513e87825fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggfun@0.0.9:", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytree@0.4.5:", type=("build", "run"))
	depends_on("r-treeio@1.8:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
