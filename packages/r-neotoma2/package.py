# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeotoma2(RPackage):
	"""Working with the Neotoma Paleoecology Database

	Access and manipulation of data using the Neotoma Paleoecology Database.
        <https://api.neotomadb.org/api-docs/>.
	"""
	
	homepage = "https://github.com/NeotomaDB/neotoma2"
	cran = "neotoma2" 

	version("1.0.3", md5="07d0ae6b85b1dbb19e5ec1fff940a18c", url="https://cran.r-project.org/src/contrib/neotoma2_1.0.3.tar.gz")
	version("1.0.2", md5="5b02b9f8fdefd32fd990d61470b72814", url="https://cran.r-project.org/src/contrib/neotoma2_1.0.2.tar.gz")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
