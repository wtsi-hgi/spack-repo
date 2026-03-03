# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnalogsea(RPackage):
	"""Interface to 'DigitalOcean'

	Provides a set of functions for interacting with the 'DigitalOcean'
    API <https://www.digitalocean.com/>, including creating images, destroying 
    them, rebooting, getting details on regions, and available images.
	"""
	
	homepage = "https://github.com/pachadotdev/analogsea"
	cran = "analogsea" 

	version("1.0.7.2", md5="9dc387a1fec29d06ea0992f35830b4c4")

	depends_on("r-httr@1.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
