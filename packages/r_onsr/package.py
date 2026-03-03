# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnsr(RPackage):
	"""Client for the 'ONS' API

	Client for the 'Office of National Statistics'
    ('ONS') API <https://api.beta.ons.gov.uk/v1>.  
	"""
	
	homepage = "https://kvasilopoulos.github.io/onsr/"
	cran = "onsr" 

	version("1.0.2", md5="8f2cbb132c4edd652dc5e8edd8b01061")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
