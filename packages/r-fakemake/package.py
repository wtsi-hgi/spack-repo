# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFakemake(RPackage):
	"""Mock the Unix Make Utility

	Use R as a minimal build system. This might come in
    handy if you are developing R packages and can not use a proper build
    system. Stay away if you can (use a proper build system).
	"""
	
	homepage = "https://gitlab.com/fvafrcu/fakemake"
	cran = "fakemake" 

	version("1.11.1", md5="70b6a6c2b874a81a5bdf1be716d46d29")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-fritools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-makefiler", type=("build", "run"))
