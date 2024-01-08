# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RFontliberation(RPackage):
	"""Liberation Fonts

	A placeholder for the Liberation fontset intended for the
    `fontquiver` package. This fontset covers the 12 combinations of
    families (sans, serif, mono) and faces (plain, bold, italic, bold
    italic) supported in R graphics devices.
	"""
	
	cran = "fontLiberation" 

	version("0.1.0", md5="7a317aca78d58fc0b2417380cc702864")

	depends_on("r@3.0:", type=("build", "run"))

