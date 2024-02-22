# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplecache(RPackage):
	"""Simply Caching R Objects

	Provides intuitive functions for caching R objects, encouraging
    reproducible, restartable, and distributed R analysis. The user selects a
    location to store caches, and then provides  nothing more than a cache name
    and instructions (R code) for how to produce the R object. Also
    provides some advanced options like environment assignments, recreating or
    reloading caches, and cluster compute bindings (using the 'batchtools'
    package) making it flexible enough for use in large-scale data analysis
    projects.
	"""
	
	homepage = "https://github.com/databio/simpleCache"
	cran = "simpleCache" 

	version("0.4.2", md5="9c06a53b3452831d7ae6ffdc415c6ed3")

