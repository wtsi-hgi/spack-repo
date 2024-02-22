# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpmaps(RPackage):
	"""Europe SpatialPolygonsDataFrame Builder

	Build custom Europe SpatialPolygonsDataFrame, if you don't know what is
    a SpatialPolygonsDataFrame see SpatialPolygons() in 'sp', by example for mapLayout() in 'antaresViz'. 
    Antares is a powerful software developed by RTE to simulate and study electric power systems 
    (more information about 'Antares' here: <https://antares-simulator.org/>).
	"""
	
	homepage = "https://github.com/rte-antares-rpackage/spMaps"
	cran = "spMaps" 

	version("0.5.0", md5="f70dcac697491ae7be48404290971b5a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp@2.0.0:", type=("build", "run"))
