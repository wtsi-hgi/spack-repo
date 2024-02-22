# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeobr(RPackage):
	"""Download Official Spatial Data Sets of Brazil

	Easy access to official spatial data sets of Brazil as 'sf' objects 
             in R. The package includes a wide range of geospatial data available
             at various geographic scales and for various years with harmonized
             attributes, projection and fixed topology.
	"""
	
	homepage = "https://ipeagit.github.io/geobr/"
	cran = "geobr" 

	version("1.8.2", md5="bd3e2dabd7227e2294498825b8576cd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-sf@0.9.3:", type=("build", "run"))
