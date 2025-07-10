# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwath2stats(RPackage):
	"""Transform and Filter SWATH Data for Statistical Packages

	This package is intended to transform SWATH data from the OpenSWATH software into a format readable by other statistics packages while performing filtering, annotation and FDR estimation.
	"""
	
	homepage = "https://peterblattmann.github.io/SWATH2stats/"
	bioc = "SWATH2stats" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SWATH2stats_1.32.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SWATH2stats/SWATH2stats_1.32.1.tar.gz"]

	version("1.32.1", sha256="7d3c599027203b12d2c83d179fc9c2f94b464992a4456ce6ba80dccb04787a92")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
