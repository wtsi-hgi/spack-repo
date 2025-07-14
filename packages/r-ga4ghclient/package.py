# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGa4ghclient(RPackage):
	"""A Bioconductor package for accessing GA4GH API data servers

	GA4GHclient provides an easy way to access public data servers through Global Alliance for Genomics and Health (GA4GH) genomics API. It provides low-level access to GA4GH API and translates response data into Bioconductor-based class objects.
	"""
	
	homepage = "https://github.com/labbcb/GA4GHclient"
	bioc = "GA4GHclient"

	version("1.32.0", commit="f71ff21fa5c7a8cee8bed9950d085766e2b2431f")
	version("1.26.0", commit="6356ce0eb70f03a8478e262b6a35c8d085692497")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
