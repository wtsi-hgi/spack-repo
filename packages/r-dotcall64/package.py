# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotcall64(RPackage):
	"""Enhanced Foreign Function Interface Supporting Long
	Vectors.

	Provides .C64(), which is an enhanced version of .C() and .Fortran() from
	the foreign function interface. .C64() supports long vectors, arguments of
	type 64-bit integer, and provides a mechanism to avoid unnecessary copies
	of read-only and write-only arguments. This makes it a convenient and fast
	interface to C/C++ and Fortran code."""

	cran = "dotCall64"

	version("1.1-1", md5="daf0febb534609e779c515d35795175c", url="https://cran.r-project.org/src/contrib/dotCall64_1.1-1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
