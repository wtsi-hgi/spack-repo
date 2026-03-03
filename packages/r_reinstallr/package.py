# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReinstallr(RPackage):
	"""Search and Install Missing Packages

	Search R files for not installed packages and run install.packages.
	"""
	
	homepage = "https://github.com/calligross/reinstallr/"
	cran = "reinstallr" 

	version("0.1.5", md5="fb121ad4ffa3d194ae4e18db877614dc")

	depends_on("r@3.3:", type=("build", "run"))
