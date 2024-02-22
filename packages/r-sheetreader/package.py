# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSheetreader(RPackage):
	"""Parse xlsx Files

	Uses C++ via the 'Rcpp' package to parse modern Excel files ('.xlsx').
    Memory usage is kept minimal by decompressing only parts of the file at a time,
    while employing multiple threads to achieve significant runtime reduction.
    Uses <https://github.com/richgel999/miniz> and <https://github.com/lemire/fast_double_parser>.
	"""
	
	homepage = "https://github.com/fhenz/SheetReader-r"
	cran = "SheetReader" 

	version("1.1.0", md5="cb828364062186d5b139e99bd432d86e")

	depends_on("r-rcpp", type=("build", "run"))
