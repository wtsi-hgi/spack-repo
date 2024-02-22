# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBufferedmatrix(RPackage):
	"""A matrix data storage object held in temporary files

	A tabular style data object where most data is stored outside main memory. A buffer is used to speed up access to data.
	"""
	
	homepage = "https://github.com/bmbolstad/BufferedMatrix"
	bioc = "BufferedMatrix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BufferedMatrix_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BufferedMatrix/BufferedMatrix_1.66.0.tar.gz"]

	version("1.66.0", md5="a4ad95db528526463e6dfca80975815e")

	depends_on("r@2.6:", type=("build", "run"))
