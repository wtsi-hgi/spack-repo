# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBufferedmatrixmethods(RPackage):
	"""Microarray Data related methods that utlize BufferedMatrix objects

	Microarray analysis methods that use BufferedMatrix objects
	"""
	
	homepage = "https://github.bom/bmbolstad/BufferedMatrixMethods"
	bioc = "BufferedMatrixMethods" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BufferedMatrixMethods_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BufferedMatrixMethods/BufferedMatrixMethods_1.66.0.tar.gz"]

	version("1.66.0", md5="57eb9e8db5a9dc58db25b88bbe5d2436")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-bufferedmatrix", type=("build", "run"))
