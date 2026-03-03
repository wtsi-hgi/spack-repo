# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsefun(RPackage):
	"""A Collection of Useful Functions by John

	A set of general functions that I have used in various 
  projects and other R packages. Miscellaneous operations
  on data frames, matrices and vectors, ROC and PR statistics.
	"""
	
	homepage = "https://github.com/bblodfon/usefun"
	cran = "usefun" 

	version("0.5.0", md5="2e984655723af23134c80449f82ee695")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-prroc@1.3.1:", type=("build", "run"))
