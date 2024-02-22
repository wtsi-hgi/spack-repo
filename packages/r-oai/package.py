# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROai(RPackage):
	"""General Purpose 'Oai-PMH' Services Client

	A general purpose client to work with any 'OAI-PMH'
    (Open Archives Initiative Protocol for 'Metadata' Harvesting) service.
    The 'OAI-PMH' protocol is described at
    <http://www.openarchives.org/OAI/openarchivesprotocol.html>.
    Functions are provided to work with the 'OAI-PMH' verbs: 'GetRecord',
    'Identify', 'ListIdentifiers', 'ListMetadataFormats', 'ListRecords', and
    'ListSets'.
	"""
	
	homepage = "https://docs.ropensci.org/oai/"
	cran = "oai" 

	version("0.4.0", md5="054ced336542744a74a4403d016fe568")

	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-httr@1.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
