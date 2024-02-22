# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoomr(RPackage):
	"""Connect to Your 'Zoom' Data

	Facilitates making a connection to the 'Zoom' API and executing
  various queries. You can use it to get data on 'Zoom' webinars and 'Zoom'
  meetings. The 'Zoom' documentation is available at 
  <https://developers.zoom.us/docs/api/>. This package is 
  not supported by 'Zoom' (owner of the software).
	"""
	
	homepage = "https://github.com/chrisumphlett/zoomr"
	cran = "zoomr" 

	version("0.2.0", md5="6faf4816c3488c76213bea38ef0b0c5f")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-janitor@2.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
