# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgutils(RPackage):
	"""Collection of Utility Functions

	
    A handy collection of utility functions designed to aid in
    package development, plotting and scientific research.  Package
    development functionalities includes among others tools such as
    cross-referencing package imports with the description file, analysis
    of redundant package imports, editing of the description file and the
    creation of package badges for GitHub.  Some of the other
    functionalities include automatic package installation and loading,
    plotting points without overlap, creating nice breaks for plots,
    overview tables and many more handy utility functions.
	"""
	
	homepage = "https://github.com/hvdboorn/hgutils"
	cran = "hgutils" 

	version("0.2.11", md5="f01c6a3242574d45c98f32b6f7113fd2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
