# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupree(RPackage):
	"""Identify Duplicated R Code in a Project

	Identifies code blocks that have a high level of similarity
  within a set of R files.
	"""
	
	homepage = "https://github.com/russHyde/dupree"
	cran = "dupree" 

	version("0.3.0", md5="e34e61e014869f55d3b65d4370473f80")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringdist@0.9.5.5:", type=("build", "run"))
	depends_on("r-lintr@2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
