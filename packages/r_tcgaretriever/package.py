# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgaretriever(RPackage):
	"""Retrieve Genomic and Clinical Data from CBioPortal Including
TCGA Data

	The Cancer Genome Atlas (TCGA) is a program aimed at improving our understanding of Cancer Biology. Several TCGA Datasets are available online. 'TCGAretriever' helps accessing and downloading TCGA data hosted on 'cBioPortal' via its Web Interface (see <https://www.cbioportal.org/> for more information).
	"""
	
	homepage = "https://www.data-pulse.com/dev_site/TCGAretriever/"
	cran = "TCGAretriever" 

	version("1.9.1", md5="48672e74dbd690cc5f4a5a42715c4e70")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
