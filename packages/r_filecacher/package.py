# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilecacher(RPackage):
	"""File Cacher

	
    The main functions in this package are with_cache() and cached_read(). 
    The former is a simple way to cache an R object into a file on disk, 
    using 'cachem'. The latter is a wrapper around any standard read function, 
    but caches both the output and the file list info. If the input file list
    info hasn't changed, the cache is used; otherwise, the original files are
    re-read. This can save time if the original operation requires reading from
    many files, and/or involves lots of processing.
	"""
	
	homepage = "https://github.com/orgadish/filecacher"
	cran = "filecacher" 

	version("0.2.9", md5="1d6e5e2eefb3cd9de200d41bb87a78f4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
