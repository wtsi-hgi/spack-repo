# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabynames(RPackage):
	"""US Baby Names 1880-2017

	US baby names provided by the SSA. This package contains all
    names used for at least 5 children of either sex.
	"""
	
	homepage = "https://github.com/hadley/babynames"
	cran = "babynames" 

	version("1.0.1", md5="deace7f35bfe1ffc2db2ea99fa0760b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
