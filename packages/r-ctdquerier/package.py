# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtdquerier(RPackage):
	"""Package for CTDbase data query, visualization and downstream analysis

	Package to retrieve and visualize data from the Comparative Toxicogenomics Database (http://ctdbase.org/). The downloaded data is formated as DataFrames for further downstream analyses.
	"""
	
	bioc = "CTDquerier" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CTDquerier_2.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CTDquerier/CTDquerier_2.10.0.tar.gz"]

	version("2.10.0", md5="42c5654d014714b22e5c1c2c2e7a2118")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
