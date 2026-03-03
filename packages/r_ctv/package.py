# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtv(RPackage):
	"""CRAN Task Views

	Infrastructure for task views to CRAN-style repositories: Querying task views and installing the associated
             packages (client-side tools), generating HTML pages and storing task view information in the repository
	     (server-side tools).
	"""
	
	homepage = "https://github.com/cran-task-views/ctv/"
	cran = "ctv" 

	version("0.9-5", md5="8227b1001c72201cdd3f941b8596b0ef")

	depends_on("r@3:", type=("build", "run"))
