# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFst(RPackage):
	"""Lightning Fast Serialization of Data Frames

	Multithreaded serialization of compressed data frames using the 'fst' format. The
    'fst' format allows for full random access of stored data and a wide range of compression
    settings using the LZ4 and ZSTD compressors.
	"""
	
	homepage = "http://www.fstpackage.org"
	cran = "fst" 

	version("0.9.8", md5="8a668f9b1616cb31036a1394402c3ee6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fstcore", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
