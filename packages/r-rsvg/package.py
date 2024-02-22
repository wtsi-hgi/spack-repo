# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsvg(RPackage):
	"""Render SVG Images into PDF, PNG, (Encapsulated) PostScript, or
Bitmap Arrays

	Renders vector-based svg images into high-quality custom-size
    bitmap arrays using 'librsvg2'. The resulting bitmap can be written to
    e.g. png, jpeg or webp format. In addition, the package can convert
    images directly to various formats such as pdf or postscript.
	"""
	
	homepage = "https://docs.ropensci.org/rsvg/"
	cran = "rsvg" 

	version("2.6.0", md5="0936b7aab088f55d727d0827a53e89d0")

	depends_on("librsvg@2:", type=("build", "link", "run"))
