# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBadger(RPackage):
	"""Badge for R Package

	Query information and generate badge for using in README and GitHub Pages.
	"""
	
	homepage = "https://github.com/GuangchuangYu/badger"
	cran = "badger" 

	version("0.2.3", md5="d6741e6f152aa4e353ae5cd40e5aa138")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dlstats", type=("build", "run"))
	depends_on("r-rvcheck", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-usethis@2:", type=("build", "run"))
