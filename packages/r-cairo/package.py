# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCairo(RPackage):
	"""R graphics device using cairo graphics library for creating high-quality
	bitmap (PNG, JPEG, TIFF), vector (PDF, SVG, PostScript) and display (X11
	and Win32) output.

	R graphics device using cairographics library that can be used to create
	high-quality vector (PDF, PostScript and SVG) and bitmap output
	(PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).
	Since it uses the same back-end for all output, copying across formats is
	WYSIWYG. Files are created without the dependence on X11 or other external
	programs. This device supports alpha channel (semi-transparent drawing) and
	resulting images can contain transparent and semi-transparent regions. It
	is ideal for use in server environments (file output) and as a replacement
	for other devices that don't have Cairo's capabilities such as alpha
	support or anti-aliasing. Backends are modular such that any subset of
	backends is supported."""

	cran = "Cairo"

	version("1.6-2", md5="335f168eee7a37b4f8e2d97b3873b8b4")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("cairo", type=("build", "link", "run"))
