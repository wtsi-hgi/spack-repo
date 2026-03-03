# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgho(RPackage):
	"""Access WHO Global Health Observatory Data from R

	Access WHO Global Health Observatory
    (<https://www.who.int/data/gho/>)
    data from R via the `OData` API
    (<https://www.who.int/data/gho/info/gho-odata-api>),
    an application program interface providing
    a simple query interface to the World
    Health Organization's data and statistics content.
	"""
	
	cran = "rgho" 

	version("3.0.2", md5="246406d0e468987def35602af66207ac")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-odataquery@0.5.3:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
