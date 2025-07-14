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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BufferedMatrix_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BufferedMatrix/BufferedMatrix_1.66.0.tar.gz"]

    version("1.72.0", tag="RELEASE_3_21")
	version("1.66.0", sha256="195ab4d499e811f6e70ce9b28cc3f1c4355298e1a15e8be1364a92ea45cf72a8")

	depends_on("r@2.6:", type=("build", "run"))
