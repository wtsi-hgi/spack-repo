# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSantoku(RPackage):
	"""A Versatile Cutting Tool

	A tool for cutting data into intervals. Allows singleton intervals.
  Always includes the whole range of data by default. Flexible labelling. 
  Convenience functions for cutting by quantiles etc. Handles dates, times, units
  and other vectors.
	"""
	
	homepage = "https://github.com/hughjonesd/santoku"
	cran = "santoku" 

	version("0.10.0", md5="d5b0e23c82c7b562b873da0247a8e3c6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
