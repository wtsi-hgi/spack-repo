# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResearchassociate(RPackage):
	"""Retrieving Publications from PubMed Database Based on User Query

	Connects to Pubmed <https://pubmed.ncbi.nlm.nih.gov/> to retrieve publications related to user-defined search query.
	"""
	
	cran = "ResearchAssociate" 

	version("1.0.1", md5="52e0e53411c30e1d3110cd976803ab46")

	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
