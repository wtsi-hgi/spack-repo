# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5lib(RPackage):
	"""hdf5 library as an R package.

	Provides C and C++ hdf5 libraries."""

	bioc = "Rhdf5lib"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rhdf5lib_1.24.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rhdf5lib/Rhdf5lib_1.24.2.tar.gz"]

	version("1.24.2", md5="d350d5309740f184ad4eec7cdb6d705b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
