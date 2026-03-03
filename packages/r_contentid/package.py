# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContentid(RPackage):
	"""An Interface for Content-Based Identifiers

	An interface for creating, registering, and resolving content-based
             identifiers for data management. Content-based identifiers rely on
             the 'cryptographic' hashes to refer to the files they identify, thus,
             anyone possessing the file can compute the identifier using a 
             well-known standard algorithm, such as 'SHA256'.  By registering
             a URL at which the content is accessible to a public archive (such as 
             Hash Archive) or depositing data in a scientific repository such 'Zenodo',
             'DataONE' or 'SoftwareHeritage', the content identifier can serve 
             many functions typically associated with A Digital Object Identifier
             ('DOI').  Unlike location-based identifiers like 'DOIs', content-based
             identifiers permit the same content to be registered in many locations.
	"""
	
	homepage = "https://github.com/cboettig/contentid"
	cran = "contentid" 

	version("0.0.18", md5="36981931566bd00892bf5b1a3a14fd4c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openssl@1.4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
