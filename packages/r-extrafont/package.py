# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RExtrafont(RPackage):
	"""Tools for Using Fonts

	Tools to using fonts other than the standard PostScript fonts.
    This package makes it easy to use system TrueType fonts and with PDF or
    PostScript output files, and with bitmap output files in Windows. extrafont
    can also be used with fonts packaged specifically to be used with, such as
    the fontcm package, which has Computer Modern PostScript fonts with math
    symbols.
	"""
	
	homepage = "https://github.com/wch/extrafont"
	cran = "extrafont" 

	version("0.19", md5="5b65dd0344de4d5e99842c602697b124")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-extrafontdb", type=("build", "run"))
	depends_on("r-rttf2pt1", type=("build", "run"))
