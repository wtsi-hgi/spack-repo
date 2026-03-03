# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemr(RPackage):
	"""Tools for Pre-Processing Emission-Excitation-Matrix (EEM)
Fluorescence Data

	Provides various tools for preprocessing Emission-Excitation-Matrix (EEM) for Parallel Factor Analysis (PARAFAC). Different
  methods are also provided to calculate common metrics such as humification index and fluorescence index.
	"""
	
	homepage = "https://github.com/PMassicotte/eemR"
	cran = "eemR" 

	version("1.0.1", md5="79047f6d0a0feab769c62ed6b18ba57e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
