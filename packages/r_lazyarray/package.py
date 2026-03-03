# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazyarray(RPackage):
	"""Persistent Large Data Array with Lazy-Loading on Demand

	Multi-threaded serialization of compressed array that 
    fully utilizes modern solid state drives. It allows 
    to store and load extremely large data on demand within seconds
    without occupying too much memories. With data stored on hard drive, 
    a lazy-array data can be loaded, shared across multiple R sessions.
    For arrays with partition mode on, multiple R sessions can write to 
    a same array simultaneously along the last dimension (partition). 
    The internal storage format is provided by 'fstcore' package geared by 
    'LZ4' and 'ZSTD' compressors.
	"""
	
	homepage = "https://github.com/dipterix/lazyarray"
	cran = "lazyarray" 

	version("1.1.0", md5="d861d222e203f92aee7bbc8d1bd06470")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-fstcore", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
