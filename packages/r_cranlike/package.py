# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCranlike(RPackage):
	"""Tools for 'CRAN'-Like Repositories

	A set of functions to manage 'CRAN'-like repositories
    efficiently.
	"""
	
	homepage = "https://github.com/r-hub/cranlike"
	cran = "cranlike" 

	version("1.0.2", md5="e05c92b83e22d36f918b0247c75da838")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-debugme", type=("build", "run"))
	depends_on("r-desc@1.1:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
