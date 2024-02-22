# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubmedMiner(RPackage):
	"""Text Mining of PubMed Abstracts

	Text mining of PubMed Abstracts (text and XML) from <https://pubmed.ncbi.nlm.nih.gov/>.
	"""
	
	cran = "pubmed.mineR" 

	version("1.0.19", md5="68bc7552ebdf49cc5d860acf6df1bb05")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
