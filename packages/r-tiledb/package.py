# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiledb(RPackage):
	"""Modern Database Engine for Multi-Modal Data via Sparse and Dense
Multidimensional Arrays

	The modern database 'TileDB' introduces a powerful on-disk
 format for multi-modal data based on dimensional arrays. It supports
 dense and sparse arrays, dataframes and key-values stores, cloud
 storage ('S3', 'GCS', 'Azure'), chunked arrays, multiple compression,
 encryption and checksum filters, uses a fully multi-threaded
 implementation, supports parallel I/O, data versioning ('time
 travel'), metadata and groups. It is implemented as an embeddable
 cross-platform C++ library with APIs from several languages, and
 integrations.
	"""
	
	homepage = "https://github.com/TileDB-Inc/TileDB-R"
	cran = "tiledb" 

	version("0.24.0", md5="514305a1b7933bc52631a767816633c7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nanotime", type=("build", "run"))
	depends_on("r-spdl", type=("build", "run"))
	depends_on("r-rcppint64", type=("build", "run"))
