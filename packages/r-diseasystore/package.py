# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiseasystore(RPackage):
	"""Feature Stores for the 'diseasy' Framework

	
  Simple feature stores and tools for creating personalised feature stores.
  'diseasystore' powers feature stores which can automatically link and aggregate features to a given stratification
  level. These feature stores are automatically time-versioned (powered by the 'SCDB' package) and allows you to easily
  and dynamically compute features as part of your continuous integration.
	"""
	
	homepage = "https://github.com/ssi-dk/diseasystore"
	cran = "diseasystore" 

	version("0.2.0", md5="880f21827587ef3d4e7c4ee254fd8330")
	version("0.1.1", md5="e7bff8beb009be5159f0666a833b5e66")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-isoweek", type=("build", "run"))
	depends_on("r-lintr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-scdb@0.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
