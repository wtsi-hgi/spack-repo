# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuca(RPackage):
	"""NEUral network-based single-Cell Annotation tool

	NeuCA is is a neural-network based method for scRNA-seq data annotation. It can automatically adjust its classification strategy depending on cell type correlations, to accurately annotate cell. NeuCA can automatically utilize the structure information of the cell types through a hierarchical tree to improve the annotation accuracy. It is especially helpful when the data contain closely correlated cell types.
	"""
	
	bioc = "NeuCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NeuCA_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NeuCA/NeuCA_1.8.1.tar.gz"]

	version("1.8.1", sha256="485a2dec6d4274556cd8e5fbd5c6025a117b20d0243eb00469928b1829d1c31c")
	version("1.8.0", commit="053e2f93a026cc1048ba2dce418f9890d2572815")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
