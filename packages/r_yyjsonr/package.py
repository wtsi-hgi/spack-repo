# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYyjsonr(RPackage):
	"""Fast JSON Parser and Generator

	A fast JSON parser, generator and validator which converts JSON 
    data to/from R objects.  The standard R data types are supported 
    (e.g. logical, numeric, integer) with configurable handling of NULL and NA 
    values. Data frames, atomic vectors and lists are all supported as data 
    containers translated to/from JSON.
    This implementation is a wrapper around the 'yyjson' 'C' library which 
    is available from <https://github.com/ibireme/yyjson>.
	"""
	
	homepage = "https://github.com/coolbutuseless/yyjsonr"
	cran = "yyjsonr" 

	version("0.1.18", md5="57bbe07d4700c485e676d6161e3e7e7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
