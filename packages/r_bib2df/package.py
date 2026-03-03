# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBib2df(RPackage):
	"""Parse a BibTeX File to a Data Frame

	Parse a BibTeX file to a data.frame to make it accessible for further analysis and visualization.
	"""
	
	homepage = "https://github.com/ropensci/bib2df"
	cran = "bib2df" 

	version("1.1.1", md5="f0d0fa25fdd9dc30130688104b0979a4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-humaniformat", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
