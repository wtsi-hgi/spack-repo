# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtts(RPackage):
	"""'data.table' Time-Series

	High-frequency time-series support via 'nanotime' and 'data.table'.
	"""
	
	cran = "dtts" 

	version("0.1.2", md5="0503fd3abd8cd8901272f6593e67b80e")

	depends_on("r-nanotime", type=("build", "run"))
	depends_on("r-data-table@1.5:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppcctz", type=("build", "run"))
	depends_on("r-rcppdate", type=("build", "run"))
