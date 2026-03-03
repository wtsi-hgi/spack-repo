# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArxiv(RPackage):
	"""Interface to the arXiv API

	An interface to the API for 'arXiv',
    a repository of electronic preprints for
    computer science, mathematics, physics, quantitative biology,
    quantitative finance, and statistics.
	"""
	
	homepage = "https://docs.ropensci.org/aRxiv/"
	cran = "aRxiv" 

	version("0.8", md5="930c0fb96f941dc17fcf6eb923bc597a")
	version("0.10", md5="f45519dd31be5c4eeff9549ef5afbc82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
