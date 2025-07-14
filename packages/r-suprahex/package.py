# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuprahex(RPackage):
	"""supraHex: a supra-hexagonal map for analysing tabular omics data

	A supra-hexagonal map is a giant hexagon on a 2-dimensional grid seamlessly consisting of smaller hexagons. It is supposed to train, analyse and visualise a high-dimensional omics input data. The supraHex is able to carry out gene clustering/meta-clustering and sample correlation, plus intuitive visualisations to facilitate exploratory analysis. More importantly, it allows for overlaying additional data onto the trained map to explore relations between input and additional data. So with supraHex, it is also possible to carry out multilayer omics data comparisons. Newly added utilities are advanced heatmap visualisation and tree-based analysis of sample relationships. Uniquely to this package, users can ultrafastly understand any tabular omics data, both scientifically and artistically, especially in a sample-specific fashion but without loss of information on large genes.
	"""
	
	homepage = "http://suprahex.r-forge.r-project.org"
	bioc = "supraHex" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/supraHex_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/supraHex/supraHex_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="a43f328168e5231e575a7464656ed9508069efcded340cf5f7eb2c243924eb6c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
