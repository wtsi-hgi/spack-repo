# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFstcore(RPackage):
	"""R Bindings to the 'Fstlib' Library

	The 'fstlib' library provides multithreaded serialization of compressed data frames using the
    'fst' format. The 'fst' format allows for random access of stored data and compression with the 'LZ4' and 'ZSTD'
    compressors.
	"""
	
	homepage = "https://www.fstpackage.org/fstcore/"
	cran = "fstcore" 

	version("0.9.18", md5="cc61fea73a170f335cccc1bbb1271cee")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
