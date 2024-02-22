# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListdown(RPackage):
	"""Create R Markdown from Lists

	Programmatically create R Markdown documents from lists.
	"""
	
	homepage = "https://github.com/kaneplusplus/listdown"
	cran = "listdown" 

	version("0.5.7", md5="c9c258a3bc58bef59413e6be7d01a727")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
