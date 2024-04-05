# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmai(RPackage):
	"""Divisia Monetary Aggregates Index

	Functions to calculate Divisia monetary aggregates index as given in Barnett, W. A. (1980) (<DOI:10.1016/0304-4076(80)90070-6>).
	"""
	
	homepage = "https://github.com/myaseen208/dmai/"
	cran = "dmai" 

	version("0.5.0", md5="00314a120b4415e274dd3e9d25c24e22")
	version("0.4.0", md5="e147cce13ab232a7a93bce5792c4ff0f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
