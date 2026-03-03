# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalettesforr(RPackage):
	"""GPL Palettes Copied from 'Gimp' and 'Inkscape'

	A set of palettes imported from 'Gimp' distributed 
  under GPL3 (<https://www.gimp.org/about/COPYING>), and 'Inkscape' 
  distributed under GPL2 (<https://inkscape.org/about/license/>).
	"""
	
	homepage = "https://github.com/frareb/palettesForR"
	cran = "palettesForR" 

	version("0.1.2", md5="d658e41435beb65496031ab32f80620d")

