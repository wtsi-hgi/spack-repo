# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleancall(RPackage):
	"""C Resource Cleanup via Exit Handlers

	Wrapper of .Call() that runs exit handlers to clean up C
    resources. Helps managing C (non-R) resources while using the R API.
	"""
	
	homepage = "https://github.com/r-lib/cleancall#readme"
	cran = "cleancall" 

	version("0.1.3", md5="041362ae308e04d3d6791e20f4c14c6f")

	depends_on("r@3.4:", type=("build", "run"))
