# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosv(RPackage):
	"""Client to Access and Operate on the 'Open Source Vulnerability'
API

	Connect, query, and operate on information available from the 
    'Open Source Vulnerability' database <https://osv.dev/>. Although 'CRAN' 
    has vulnerabilities listed, these are few compared to projects such as 
    'PyPI'. With tighter integration between 'R' and 'Python', having an 
    'R' specific package to access details about vulnerabilities from 
    various sources is a worthwhile enterprise.
	"""
	
	homepage = "https://al-obrien.github.io/rosv/"
	cran = "rosv" 

	version("0.5.1", md5="8f9583adeaa2b22d5632fe546393f54e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-digest@0.6:", type=("build", "run"))
	depends_on("r-furrr@0.3:", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
