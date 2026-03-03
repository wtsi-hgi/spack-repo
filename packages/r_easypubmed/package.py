# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasypubmed(RPackage):
	"""Search and Retrieve Scientific Publication Records from PubMed

	Query NCBI Entrez and retrieve PubMed records in XML or text format. Process PubMed records by extracting and aggregating data from selected fields. A large number of records can be easily downloaded via this simple-to-use interface to the NCBI PubMed API.
	"""
	
	homepage = "https://www.data-pulse.com/dev_site/easypubmed/"
	cran = "easyPubMed" 

	version("2.13", md5="80c00e06855791697f4890fa86ce1185")

	depends_on("r@3.1:", type=("build", "run"))
