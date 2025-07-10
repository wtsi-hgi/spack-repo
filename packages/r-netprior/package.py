# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetprior(RPackage):
	"""A model for network-based prioritisation of genes

	A model for semi-supervised prioritisation of genes integrating network data, phenotypes and additional prior knowledge about TP and TN gene labels from the literature or experts.
	"""
	
	homepage = "http://bioconductor.org/packages/netprioR"
	bioc = "netprioR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/netprioR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/netprioR/netprioR_1.28.0.tar.gz"]

	version("1.28.0", sha256="913b56763c125c2729a51c0a550b5533ad511a4bdd310f9ff4c52f7abb4c0b0a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-sparsemvn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
