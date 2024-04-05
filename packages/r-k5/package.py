# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RK5(RPackage):
	"""Kiernan Nicholls Miscellaneous

	Quality of life functions for interactive programming.
    Shortcuts for common combinations of functions or different default
    arguments. Not to be used in production level scripts, but useful for
    exploring and quickly manipulating data for easy analysis. Also
    imports a variety of packages to facilitate the installation of those
    imported packages on the host machine.
	"""
	
	homepage = "https://k5cents.github.io/k5/"
	cran = "k5" 

	version("0.2.1", md5="a6bb389b79d780754a545e88a1571151", url="https://cran.r-project.org/src/contrib/k5_0.2.1.tar.gz")
	version("0.0.5", md5="45d50882a1951a871a1c541ec16e9d05", url="https://cran.r-project.org/src/contrib/k5_0.0.5.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clipr@0.8:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-fs@1.6.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lubridate@1.9.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-usethis@2.2.2:", type=("build", "run"))
