# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystemfonts(RPackage):
	"""System Native Font Finding.

	Provides system native access to the font catalogue. As font handling
	varies between systems it is difficult to correctly locate installed fonts
	across different operating systems. The 'systemfonts' package provides
	bindings to the native libraries on Windows, macOS and Linux for finding
	font files that can then be used further by e.g. graphic devices. The main
	use is intended to be from compiled code but 'systemfonts' also provides
	access from R."""

	cran = "systemfonts"

	license("MIT")

	version("1.0.6", md5="a64862faca6ec5e67a0381bc0eb300be")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cpp11@0.2.1:", type=("build", "run"))
	depends_on("fontconfig", type=("build", "link", "run"))
	depends_on("freetype@2:", type=("build", "link", "run"))
