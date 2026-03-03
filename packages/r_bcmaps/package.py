# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcmaps(RPackage):
	"""Map Layers and Spatial Utilities for British Columbia

	Various layers of B.C., including administrative boundaries,
    natural resource management boundaries, census boundaries etc. All
    layers are available in BC Albers
    (<https://spatialreference.org/ref/epsg/3005/>) equal-area
    projection, which is the B.C. government standard. The layers are
    sourced from the British Columbia and Canadian government under open
    licenses, including B.C. Data Catalogue (<https://data.gov.bc.ca>),
    the Government of Canada Open Data Portal
    (<https://open.canada.ca/en/using-open-data>), and Statistics Canada
    (<https://www.statcan.gc.ca/en/reference/licence>).
	"""
	
	homepage = "https://github.com/bcgov/bcmaps"
	cran = "bcmaps" 

	version("2.2.0", md5="d5984a0c2aca2a33fc79b393d940e257")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-bcdata@0.4.1:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
