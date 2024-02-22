# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtubase(RPackage):
	"""Provides structure and functions for the analysis of OTU data

	Provides a platform for Operational Taxonomic Unit based analysis
	"""
	
	bioc = "OTUbase" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/OTUbase_1.52.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/OTUbase/OTUbase_1.52.0.tar.gz"]

	version("1.52.0", md5="612c0f07995eb5cc0f753eb6750e5216")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread@1.23.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
