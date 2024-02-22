# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThinkr(RPackage):
	"""Tools for Cleaning Up Messy Files

	Some tools for cleaning up messy 'Excel' files to be suitable
    for R. People who have been working with 'Excel' for years built more
    or less complicated sheets with names, characters, formats that are
    not homogeneous. To be able to use them in R nowadays, we built a set
    of functions that will avoid the majority of importation problems and
    keep all the data at best.
	"""
	
	homepage = "https://github.com/Thinkr-open/thinkr"
	cran = "thinkr" 

	version("0.16", md5="0839448dadf7711a7b63f3f968fb6dde")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-rvg", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
