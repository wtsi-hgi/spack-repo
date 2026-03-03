# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRorcid(RPackage):
	"""Interface to the 'Orcid.org' API

	Client for the 'Orcid.org' API (<https://orcid.org/>).
    Functions included for searching for people, searching by 'DOI',
    and searching by 'Orcid' 'ID'.
	"""
	
	homepage = "https://github.com/ropensci/rorcid"
	cran = "rorcid" 

	version("0.7.0", md5="e9f0e42388d7cea65efb46a1ca53d813")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-fauxpas@0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
