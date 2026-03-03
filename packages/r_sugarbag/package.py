# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSugarbag(RPackage):
	"""Create Tessellated Hexagon Maps

	Create a hexagon tile map display from spatial polygons. Each 
    polygon is represented by a hexagon tile, placed as close to it's original
    centroid as possible, with a focus on maintaining spatial relationship to
    a focal point. Developed to aid visualisation and analysis of spatial 
    distributions across Australia, which can be challenging due to the 
    concentration of the population on the coast and wide open interior.
	"""
	
	homepage = "https://srkobakian.github.io/sugarbag/"
	cran = "sugarbag" 

	version("0.1.6", md5="9a9faef2216c43d9a4b57bc2102e141f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-geosphere@1.5:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-rmapshaper@0.4.6:", type=("build", "run"))
	depends_on("r-sf@1.0.8:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
