# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMilor(RPackage):
	"""Differential neighbourhood abundance testing on a graph

	Milo performs single-cell differential abundance testing. Cell states are modelled as representative neighbourhoods on a nearest neighbour graph. Hypothesis testing is performed using a negative bionomial generalized linear model.
	"""
	
	homepage = "https://marionilab.github.io/miloR"
	bioc = "miloR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miloR_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miloR/miloR_1.10.0.tar.gz"]

	version("2.0.0", md5="f02be1539df5c6cfd31ae8042f78f274", url="https://bioconductor.org/packages/3.19/bioc/src/contrib/miloR_2.0.0.tar.gz")
	version("1.10.0", md5="9ab9a4a2fe26786cd8fef69354bfa08f")
	version("1.2.0", md5="a7f60672a41a27d56278f108c532f347", url="https://bioconductor.org/packages/3.14/bioc/src/contrib/miloR_1.2.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"), when="@2.0.0:")
