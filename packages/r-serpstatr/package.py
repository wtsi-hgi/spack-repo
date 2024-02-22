# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerpstatr(RPackage):
	"""'Serpstat' API Wrapper

	The primary goal of 'Serpstat' API <https://serpstat.com/api/> 
    is to reduce manual SEO (search engine optimization) and PPC (pay-per-click) 
    tasks. You can automate your keywords research or competitors analysis 
    with this API wrapper.
	"""
	
	homepage = "https://serpstat.com/api/"
	cran = "serpstatr" 

	version("0.2.1", md5="2ec4066be79a69508969e267e21425d9")

	depends_on("r-httr@1.4.1:", type=("build", "run"))
