# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrioritizrdata(RPackage):
	"""Conservation Planning Datasets

	Conservation planning datasets for learning how to use the
    'prioritizr' package <https://CRAN.R-project.org/package=prioritizr>.
	"""
	
	homepage = "https://prioritizr.github.io/prioritizrdata/"
	cran = "prioritizrdata" 

	version("0.3.2", md5="2bdb457b61edaa95b6c998fd005a99c8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra@1.6.53:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
