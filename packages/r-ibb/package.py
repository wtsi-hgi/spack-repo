# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbb(RPackage):
	"""R Wrapper for Istanbul Municipality Open Data Portal

	Call wrappers for Istanbul Metropolitan
    Municipality's Open Data Portal (Turkish: İstanbul Büyükşehir
    Belediyesi Açık Veri Portalı) at <https://data.ibb.gov.tr/en/>.
	"""
	
	homepage = "https://github.com/berkorbay/ibb"
	cran = "ibb" 

	version("0.0.2", md5="1d0a7394ed791c6d577ab545e5c43ae8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
