# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDateutils(RPackage):
	"""Date Utils

	Utilities for mixed frequency data. In particular, use to aggregate and normalize tabular mixed frequency data, index dates to end of period, and seasonally adjust tabular data.
	"""
	
	homepage = "https://github.com/macroeconomicdata/dateutils"
	cran = "dateutils" 

	version("0.1.5", md5="f53c0e719de0ef067aacc4ff1730298c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
