# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcltk2(RPackage):
	"""Tcl/Tk Additions

	A series of additional Tcl commands and Tk widgets with style
  and various functions (under Windows: DDE exchange, access to the
  registry and icon manipulation) to supplement the tcltk package
	"""
	
	homepage = "http://www.sciviews.org/SciViews-R"
	cran = "tcltk2" 

	version("1.2-11", md5="8c2bb042e85986436eaf4b3e49e242ec", url="https://cran.r-project.org/src/contrib/tcltk2_1.2-11.tar.gz")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("tcl@8.5:", type=("build", "link", "run"))
	depends_on("tk@8.5:", type=("build", "link", "run"))
	depends_on("tktable", type=("build", "link", "run"))
