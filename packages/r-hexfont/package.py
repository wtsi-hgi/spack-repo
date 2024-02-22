# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHexfont(RPackage):
	"""'GNU Unifont' Hex Fonts

	Contains most of the hex font files from the 'GNU Unifont Project' <https://unifoundry.com/unifont/> compressed by 'xz'.  'GNU Unifont' is a duospaced bitmap font that attempts to cover all the official Unicode glyphs plus several of the artificial scripts in the '(Under-)ConScript Unicode Registry' <http://www.kreativekorp.com/ucsur/>.  Provides a convenience function for loading in several of them at the same time as a 'bittermelon' bitmap font object for easy rendering of the glyphs in an 'R' terminal or graphics device.
	"""
	
	homepage = "https://github.com/trevorld/hexfont"
	cran = "hexfont" 

	version("0.4.0", md5="e53ef598980c3cb47087b008951f90ec")

	depends_on("r-bittermelon@1.1.2:", type=("build", "run"))
