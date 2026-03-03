# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjsoncons(RPackage):
	"""'C++' Header-Only 'jsoncons' Library for 'JSON' Queries

	The 'jsoncons'
    <https://danielaparker.github.io/jsoncons/> 'C++' header-only
    library constructs representations from a 'JSON' character vector,
    and provides extensions for flexible queries and other operations
    on 'JSON' objects. This package provides 'R' functions to query
    (filter or transform) and pivot (convert from array-of-objects to
    object-of-arrays, for easy import into 'R') 'JSON' or 'NDJSON'
    strings or files using 'JSONpointer', 'JSONpath' or 'JMESpath'
    expression. The 'jsoncons' library is also be easily linked to
    other packages for direct access to 'C++' functionality.
	"""
	
	homepage = "https://mtmorgan.github.io/rjsoncons/"
	cran = "rjsoncons" 

	version("1.2.0", md5="42e461e866294c1912d3374fb66d174b")

	depends_on("r-cpp11", type=("build", "run"))
