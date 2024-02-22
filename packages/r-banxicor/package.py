# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanxicor(RPackage):
	"""Download Data from the Bank of Mexico

	Provides functions to scrape IQY calls to Bank of Mexico,
    downloading and ordering the data conveniently.
	"""
	
	cran = "banxicoR" 

	version("0.9.0", md5="c3d8348968ab17326d15c56a48fc23a1")

	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
