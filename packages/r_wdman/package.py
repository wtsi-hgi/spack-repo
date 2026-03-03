# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdman(RPackage):
	"""'Webdriver'/'Selenium' Binary Manager

	There are a number of binary files associated with the
    'Webdriver'/'Selenium' project. This package provides functions to download
    these binaries and to manage processes involving them.
	"""
	
	homepage = "https://docs.ropensci.org/wdman/"
	cran = "wdman" 

	version("0.2.6", md5="32579f4a2eb8c153d44714787ee688c0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-binman", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-semver@0.2:", type=("build", "run"))
