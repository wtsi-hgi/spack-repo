# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplercache(RPackage):
	"""Simple R Cache

	Simple result caching in R based on R.cache. The global environment is not 
    considered when caching results simplifying moving files between multiple instances 
    of R. Relies on more base functions than R.cache (e.g. cached results are saved using 
    saveRDS() and readRDS()).
	"""
	
	cran = "simpleRCache" 

	version("0.3.3", md5="2308f6acfa28e9e1c48d290801e108eb")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
