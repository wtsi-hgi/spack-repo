# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBags(RPackage):
	"""A Bayesian Approach for Geneset Selection

	R package providing functions to perform geneset significance analysis over simple cross-sectional data between 2 and 5 phenotypes of interest.
	"""
	
	bioc = "BAGS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BAGS_2.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BAGS/BAGS_2.42.0.tar.gz"]

	version("2.42.0", md5="42c7a57422ddbb5c2d5263703a7e22d0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-breastcancervdx", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
