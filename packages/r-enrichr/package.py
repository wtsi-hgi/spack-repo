# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichr(RPackage):
	"""Provides an R Interface to 'Enrichr'

	Provides an R interface to all 'Enrichr' databases. 'Enrichr' is a web-based tool for analysing gene sets and returns any enrichment of common annotated biological features. Quoting from their website 'Enrichment analysis is a computational method for inferring knowledge about an input gene set by comparing it to annotated gene sets representing prior biological knowledge.' See <https://maayanlab.cloud/Enrichr/> for further details.
	"""
	
	cran = "enrichR" 

	version("3.2", md5="998939d80840cc81b1e45b1f78fcdb69")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
