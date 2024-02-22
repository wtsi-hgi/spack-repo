# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdpar(RPackage):
	"""Interface to the World Database on Protected Areas

	Fetch and clean data from the World Database on Protected
    Areas (WDPA) and the World Database on Other Effective Area-Based
    Conservation Measures (WDOECM). Data is obtained from Protected Planet
    <https://www.protectedplanet.net/en>. To augment data cleaning procedures,
    users can install the 'prepr' R package (available at
    <https://github.com/dickoa/prepr>). For more information on this package,
    see Hanson (2022) <doi:10.21105/joss.04594>.
	"""
	
	homepage = "https://prioritizr.github.io/wdpar/"
	cran = "wdpar" 

	version("1.3.7", md5="3b2d3577e5f8849f6ece841abdebc9c6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.13:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-curl@3.2:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-countrycode@1.1:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
	depends_on("r-webdriver@1.0.6:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-cli@1.0.1:", type=("build", "run"))
	depends_on("r-lwgeom@0.2.1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-pingr@1.1.2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
