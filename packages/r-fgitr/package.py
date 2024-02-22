# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgitr(RPackage):
	"""Using 'FastGit' to Accelerate the Access to 'GitHub'

	'FastGit' <https://doc.fastgit.org/> works like a mirror of 'GitHub' to make significant acceleration. 'fgitR' is a package to do git operation with 'FastGit' automatically.
	"""
	
	cran = "fgitR" 

	version("0.2.0", md5="7e73fd477bdf3a72dcbea214b55480f9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
