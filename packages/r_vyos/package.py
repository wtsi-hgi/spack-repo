# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVyos(RPackage):
	"""Interface for Multiple Data Providers 'EDDS' and 'FRED'

	Interface for multiple data sources, such as the 
    'EDDS' API <https://evds2.tcmb.gov.tr/index.php?/evds/userDocs> of the 
    Central Bank of the Republic of Türkiye and the 
    'FRED' API <https://fred.stlouisfed.org/docs/api/fred/> of the Federal Reserve Bank. 
    Both data providers require API keys for access, which users can easily obtain 
    by creating accounts on their respective websites. 
    The package provides caching ability with the selection of periods to increase the 
    speed and efficiency of requests. 
    It combines datasets requested from different sources, 
    helping users when the data has common frequencies. 
    While combining data frames whenever possible, it also keeps all requested data
    available as separate data frames to increase efficiency.
	"""
	
	homepage = "https://github.com/spvyos/vyos"
	cran = "vyos" 

	version("1.0.2", md5="0f96501ea0eaa8bef6118588a1258f48")

	depends_on("r@3.4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
