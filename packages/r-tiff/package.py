# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiff(RPackage):
	"""Read and write TIFF images.

	This package provides an easy and simple way to read, write and display
	bitmap images stored in the TIFF format. It can read and write both files
	and in-memory raw vectors."""

	cran = "tiff"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("0.1-12", md5="2e24ff9e6afffa8243c6d1a5356aa374")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
