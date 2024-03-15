# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHipread(RPackage):
	"""Read Hierarchical Fixed Width Files

	Read hierarchical fixed width files like those commonly used by 
    many census data providers. Also allows for reading of data in chunks,
    and reading 'gzipped' files without storing the full file in memory.
	"""
	
	cran = "hipread" 

	version("0.2.4", md5="50d837f9ced720692ad61f0a3544ace4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
