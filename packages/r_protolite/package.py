# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtolite(RPackage):
	"""Highly Optimized Protocol Buffer Serializers

	Pure C++ implementations for reading and writing several common data 
    formats based on Google protocol-buffers. Currently supports 'rexp.proto' for 
    serialized R objects, 'geobuf.proto' for binary geojson, and 'mvt.proto' for 
    vector tiles. This package uses the auto-generated C++ code by protobuf-compiler, 
    hence the entire serialization is optimized at compile time. The 'RProtoBuf' 
    package on the other hand uses the protobuf runtime library to provide a general-
    purpose toolkit for reading and writing arbitrary protocol-buffer data in R.
	"""
	
	homepage = "https://github.com/jeroen/protolite"
	cran = "protolite" 

	version("2.3.0", md5="7c76e71112d0d88673e133d126ff46ad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
