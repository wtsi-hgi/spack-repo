# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMongolite(RPackage):
	"""Fast and Simple 'MongoDB' Client for R

	High-performance MongoDB client based on 'mongo-c-driver' and 'jsonlite'.
    Includes support for aggregation, indexing, map-reduce, streaming, encryption,
    enterprise authentication, and GridFS. The online user manual provides an overview 
    of the available methods in the package: <https://jeroen.github.io/mongolite/>.
	"""
	
	homepage = "https://github.com/jeroen/mongolite/"
	cran = "mongolite" 

	version("2.7.3", md5="49991fa458d38c15e4f6c4daf5882cc9")

	depends_on("r-jsonlite@1.4:", type=("build", "run"))
	depends_on("r-openssl@1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("openssl", type=("build", "link", "run"))
	depends_on("cyrus-sasl", type=("build", "link", "run"))
