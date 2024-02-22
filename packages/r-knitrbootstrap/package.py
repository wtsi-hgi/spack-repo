# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitrbootstrap(RPackage):
	"""'knitr' Bootstrap Framework

	A framework to create Bootstrap <https://getbootstrap.com/> HTML reports from 'knitr'
    'rmarkdown'.
	"""
	
	homepage = "https://github.com/jimhester/knitrBootstrap#readme"
	cran = "knitrBootstrap" 

	version("1.0.3", md5="2d6dbdc00f5d80833bdc767c682ebbfb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-knitr@1.5.25:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
