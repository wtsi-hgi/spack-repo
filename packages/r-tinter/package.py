# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinter(RPackage):
	"""Generate a Monochromatic Palette

	Generate a palette of tints, shades or both from a single colour.
	"""
	
	homepage = "https://github.com/poissonconsulting/tinter"
	cran = "tinter" 

	version("0.1.0", md5="a9ca6ed027ea0ee350741d71ef9b103e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
