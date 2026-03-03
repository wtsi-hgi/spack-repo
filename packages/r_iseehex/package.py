# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseehex(RPackage):
	"""iSEE extension for summarising data points in hexagonal bins

	This package provides panels summarising data points in hexagonal bins for `iSEE`. It is part of `iSEEu`, the iSEE universe of panels that extend the `iSEE` package.
	"""
	
	homepage = "https://github.com/iSEE/iSEEhex"
	bioc = "iSEEhex" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSEEhex_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSEEhex/iSEEhex_1.4.0.tar.gz"]

	version("1.4.0", md5="9bc98dc14114c756f97c130adf061a4b")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-isee", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
