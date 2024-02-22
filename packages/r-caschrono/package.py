# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaschrono(RPackage):
	"""Series Temporelles Avec R

	Functions, data sets and exercises solutions for the book Series Temporelles Avec R (Yves Aragon, edp sciences, 2016). For all chapters, a vignette is available with some additional material and exercises solutions.
	"""
	
	cran = "caschrono" 

	version("2.4", md5="e7ba1f62d1fad8aa4fb38a056fef03f5")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
