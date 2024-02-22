# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSapfluxnetr(RPackage):
	"""Working with 'Sapfluxnet' Project Data

	Access, modify, aggregate and plot data from the 'Sapfluxnet' project
  (<http://sapfluxnet.creaf.cat>), the first global database of sap flow measurements.
	"""
	
	homepage = "https://github.com/sapfluxnet/sapfluxnetr"
	cran = "sapfluxnetr" 

	version("0.1.4", md5="f088d13de1fa9ee82899b638b07290a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
