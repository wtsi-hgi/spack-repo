# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZlibbioc(RPackage):
	"""An R packaged zlib-1.2.5.

	This package uses the source code of zlib-1.2.5 to create libraries for
	systems that do not have these available via other means (most Linux and
	Mac users should have system-level access to zlib, and no direct need
	for this package). See the vignette for instructions on use."""

	bioc = "zlibbioc"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/zlibbioc_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/zlibbioc/zlibbioc_1.48.0.tar.gz"]

	version("1.48.0", md5="babdaf77bc9e9e8218fa07d643f31730")

