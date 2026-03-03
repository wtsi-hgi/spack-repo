# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRglobi(RPackage):
	"""Interface to Global Biotic Interactions

	A programmatic interface to the web service methods
    provided by Global Biotic Interactions (GloBI)
    (<https://www.globalbioticinteractions.org/>). GloBI provides 
    access to spatial-temporal species interaction records from 
    sources all over the world. rglobi provides methods to search 
    species interactions by location, interaction type, and 
    taxonomic name.
	"""
	
	homepage = "https://docs.ropensci.org/rglobi/"
	cran = "rglobi" 

	version("0.3.4", md5="48b4d3da98063da73b058dca9338fef8")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rcurl@0.3.4:", type=("build", "run"))
	depends_on("r-curl@0.3.3:", type=("build", "run"))
