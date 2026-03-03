# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatsoc(RPackage):
	"""Group Animal Relocation Data by Spatial and Temporal
Relationship

	Detects spatial and temporal groups in GPS relocations
    (Robitaille et al. (2019) <doi:10.1111/2041-210X.13215>).  It can be
    used to convert GPS relocations to gambit-of-the-group format to build
    proximity-based social networks In addition, the randomizations
    function provides data-stream randomization methods suitable for GPS
    data.
	"""
	
	homepage = "https://docs.ropensci.org/spatsoc/"
	cran = "spatsoc" 

	version("0.2.2", md5="687c2bf91074630cd496d28d3632cdfd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-adehabitathr@0.4.21:", type=("build", "run"))
	depends_on("r-data-table@1.10.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
