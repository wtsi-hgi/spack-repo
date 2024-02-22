# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeatranges(RPackage):
	"""Tidy Up Date/Time Ranges

	Collapse, partition, combine, fill gaps in and expand date/time ranges.
	"""
	
	homepage = "https://github.com/arg0naut91/neatRanges"
	cran = "neatRanges" 

	version("0.1.4", md5="78c742e1c3e67c53dc7c2922a4e9ab56")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
