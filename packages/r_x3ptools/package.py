# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RX3ptools(RPackage):
	"""Tools for Working with 3D Surface Measurements

	The x3p file format  is specified in ISO standard 5436:2000 to 
    describe 3d surface measurements. 'x3ptools' allows reading, writing and 
    basic modifications to the 3D surface measurements.
	"""
	
	homepage = "https://github.com/heike/x3ptools"
	cran = "x3ptools" 

	version("0.0.4", md5="7e18ee5b2b881fac420c8a88efc6bdac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-digest@0.6:", type=("build", "run"))
	depends_on("r-xml2@1.3.5:", type=("build", "run"))
	depends_on("r-rgl@1.2:", type=("build", "run"))
	depends_on("r-zoo@1.8:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-pracma@2.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-yaml@2.3.7:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-imager@0.45.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
