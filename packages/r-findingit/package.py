# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindingit(RPackage):
	"""Find Pattern in Files of All Branches of a 'git' Repository

	Creates a HTML widget which displays the results of searching for a pattern in files in a given 'git' repository, including all its branches. The results can also be returned in a dataframe.
	"""
	
	homepage = "https://github.com/stla/findInGit"
	cran = "findInGit" 

	version("0.1.1", md5="efd1ba3892ec31a1f230c653f670461e")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
