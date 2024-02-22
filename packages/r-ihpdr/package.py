# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIhpdr(RPackage):
	"""Download Data from the International House Price Database

	Web scraping the <https://www.dallasfed.org> for
    up-to-date data on international house prices and exuberance
    indicators. Download data in tidy format.
	"""
	
	homepage = "https://github.com/kvasilopoulos/ihpdr"
	cran = "ihpdr" 

	version("1.2.1", md5="c217c92bf4d18c8ca51563f9c5d24194")

	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rvest@0.3.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
