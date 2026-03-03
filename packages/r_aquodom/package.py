# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAquodom(RPackage):
	"""Access to Aquo domaintables from R (Dutch)

	The Aquo Standard is the Dutch Standard for the exchange of 
    data in water management. With *aquodom* (short for aquo domaintables) 
    it is easy to exploit the API (<https://www.aquo.nl/index.php/Hoofdpagina>) to download domaintables 
    of the Aquo Standard and use them in R.
	"""
	
	homepage = "https://redtent.github.io/aquodom/"
	cran = "aquodom" 

	version("0.1.1", md5="70334d0fe56acb441c234a531faebd49")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
