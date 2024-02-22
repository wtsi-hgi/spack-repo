# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmastats(RPackage):
	"""Download Weather Data from Japan Meteorological Agency Website

	Provides features that allow users to download 
  weather data published by the Japan Meteorological Agency (JMA) website 
  (<https://www.jma.go.jp/jma/index.html>). The data includes information 
  dating back to 1976 and aligns with the categories available on the website. 
  Additionally, users can process the best track data of typhoons and easily 
  handle earthquake record files.
	"""
	
	homepage = "https://github.com/uribo/jmastats"
	cran = "jmastats" 

	version("0.2.0", md5="8f31725ee4b999c2d852eea23cf30da6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-forcats@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-sf@0.6.3:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-units@0.5.1:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
