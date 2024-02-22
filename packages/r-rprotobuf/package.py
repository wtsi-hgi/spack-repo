# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprotobuf(RPackage):
	"""R Interface to the 'Protocol Buffers' 'API' (Version 2 or 3)

	Protocol Buffers are a way of encoding structured data in an
 efficient yet extensible format. Google uses Protocol Buffers for almost all
 of its internal 'RPC' protocols and file formats.  Additional documentation
 is available in two included vignettes one of which corresponds to our 'JSS'
 paper (2016, <doi:10.18637/jss.v071.i02>. A sufficiently recent version of
 'Protocol Buffers' library is required; currently version 3.3.0 from 2017
 is the stated minimum.
	"""
	
	homepage = "https://github.com/eddelbuettel/rprotobuf"
	cran = "RProtoBuf" 

	version("0.4.22", md5="5dba20d2aa24bdae9d9eef72b71fdc92")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
