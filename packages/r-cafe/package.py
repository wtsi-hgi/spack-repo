# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCafe(RPackage):
	"""Chromosmal Aberrations Finder in Expression data

	Detection and visualizations of gross chromosomal aberrations using Affymetrix expression microarrays as input
	"""
	
	bioc = "CAFE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CAFE_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CAFE/CAFE_1.38.0.tar.gz"]

	version("1.38.0", md5="1a64370f203f198ad86163715decbebb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
