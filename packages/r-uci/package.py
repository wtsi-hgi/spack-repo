# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUci(RPackage):
	"""Urban Centrality Index

	Calculates the Urban Centrality Index (UCI) as in Pereira et al., 
             (2013) <doi:10.1111/gean.12002>. The UCI measures the 
             extent to which the spatial organization of a city or region varies 
             from extreme polycentric to extreme monocentric in a continuous 
             scale from 0 to 1. Values closer to 0 indicate more polycentric patterns
             and values closer to 1 indicate a more monocentric urban form.
	"""
	
	homepage = "https://github.com/ipeaGIT/uci"
	cran = "uci" 

	version("0.3.0", md5="4c04ca9d45aa01701792d59b621d5381")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cpprouting", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
