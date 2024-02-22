# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCder(RPackage):
	"""Interface to the California Data Exchange Center (CDEC)

	Connect to the California Data Exchange Center (CDEC) 
    Web Service <http://cdec.water.ca.gov/>. 'CDEC' provides a centralized 
    database to store, process, and exchange real-time hydrologic information 
    gathered by various cooperators throughout California. The 'CDEC' Web Service 
    <http://cdec.water.ca.gov/dynamicapp/wsSensorData> provides a data download 
    service for accessing historical records. 
	"""
	
	homepage = "https://github.com/mkoohafkan/cder"
	cran = "cder" 

	version("0.3-1", md5="de8b3d2fa3e3b81246e11b93d9cc34df")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
