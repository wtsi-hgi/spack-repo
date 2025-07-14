# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNethet(RPackage):
	"""A bioconductor package for high-dimensional exploration of biological network heterogeneity

	Package nethet is an implementation of statistical solid methodology enabling the analysis of network heterogeneity from high-dimensional data. It combines several implementations of recent statistical innovations useful for estimation and comparison of networks in a heterogeneous, high-dimensional setting. In particular, we provide code for formal two-sample testing in Gaussian graphical models (differential network and GGM-GSA; Stadler and Mukherjee, 2013, 2014) and make a novel network-based clustering algorithm available (mixed graphical lasso, Stadler and Mukherjee, 2013).
	"""
	
	bioc = "nethet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nethet_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nethet/nethet_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="12ea69f6eece283c169874ced85c70a4d3401094830a732730ffd178fcdc464b")

	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-genenet", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
