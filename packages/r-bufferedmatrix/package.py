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

	version("1.72.0", commit="aa9e63439f425c098785232e98902633849e098b")
	version("1.66.0", commit="1feca4469540f3c0a15f75715f2e69b93310c451")

	depends_on("r@2.6:", type=("build", "run"))
