# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdigenr(RPackage):
	"""Research Project Directory Generator

	Create a project directory structure, along with typical files
    for that project.  This allows projects to be quickly and easily created,
    as well as for them to be standardized. Designed specifically with scientists
    in mind (mainly bio-medical researchers, but likely applies to other fields).
	"""
	
	homepage = "https://github.com/rostools/prodigenr"
	cran = "prodigenr" 

	version("0.6.2", md5="fdf063cc3df59b9065037200a979be56")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
