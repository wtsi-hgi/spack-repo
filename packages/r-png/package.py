# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPng(RPackage):
	"""Read and write PNG images.

	This package provides an easy and simple way to read, write and display
	bitmap images stored in the PNG format. It can read and write both files
	and in-memory raw vectors."""

	cran = "png"

	version("0.1-8", md5="5667528b7bbdd8c058018ea7ac6573a7")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
