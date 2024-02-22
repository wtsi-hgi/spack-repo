# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCimir(RPackage):
	"""Interface to the CIMIS Web API

	Connect to the California Irrigation Management 
    Information System (CIMIS) Web API. See the CIMIS main page 
    <https://cimis.water.ca.gov> and web API documentation
    <https://et.water.ca.gov> for more information.
	"""
	
	homepage = "https://github.com/mkoohafkan/cimir"
	cran = "cimir" 

	version("0.4-1", md5="becf348688f727c8960010e100104937")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
