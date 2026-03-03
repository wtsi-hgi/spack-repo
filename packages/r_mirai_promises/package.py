# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiraiPromises(RPackage):
	"""Make 'Mirai' 'Promises'

	Allows 'mirai' objects encapsulating asynchronous computations,
    from the 'mirai' package by Gao (2023) <doi:10.5281/zenodo.7912722>, to be
    used interchangeably with 'promise' objects from the 'promises' package by
    Cheng (2021) <https://CRAN.R-project.org/package=promises>. This facilitates
    their use with packages 'plumber' by Schloerke and Allen (2022)
    <https://CRAN.R-project.org/package=plumber> and 'shiny' by Cheng, Allaire,
    Sievert, Schloerke, Xie, Allen, McPherson, Dipert and Borges (2022)
    <https://CRAN.R-project.org/package=shiny>.
	"""
	
	homepage = "https://shikokuchuo.net/mirai.promises/"
	cran = "mirai.promises" 

	version("0.4.1", md5="ae4e86386f2eb92fa82cba5f42b85ddc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nanonext@0.10.1:", type=("build", "run"))
	depends_on("r-promises@1.1:", type=("build", "run"))
