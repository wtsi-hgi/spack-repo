# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChanger(RPackage):
	"""Change R Package Name

	Changing the name of an existing R package is annoying but common task especially in the early stages of package development. This package (mostly) automates this task.
	"""
	
	homepage = "https://github.com/helske/changer"
	cran = "changer" 

	version("0.0.5", md5="0eadda943b75f9aec378bdd438ae3e83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-available", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
