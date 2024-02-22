# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMongopipe(RPackage):
	"""Query MongoDB Documents with R

	Translate R code into MongoDB aggregation pipelines.
	"""
	
	homepage = "https://rpkgs.gitlab.io/mongopipe"
	cran = "mongopipe" 

	version("0.1.1", md5="0dad5849d3feb5860a1b73b5c0a1ac69")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
