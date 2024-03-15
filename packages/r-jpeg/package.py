# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpeg(RPackage):
	"""Read and write JPEG images.

	This package provides an easy and simple way to read, write and display
	bitmap images stored in the JPEG format. It can read and write both files
	and in-memory raw vectors."""

	cran = "jpeg"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("0.1-10", md5="a8b2893917c1766343f0876459784435")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
