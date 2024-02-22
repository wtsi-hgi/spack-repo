# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBstools(RPackage):
	"""Create HTML Content with Bootstrap 5 Classes and Layouts

	Functions are pre-configured to utilize Bootstrap 5 classes and 
  HTML structures to create Bootstrap-styled HTML quickly and easily. Includes 
  functions for creating common Bootstrap elements such as containers, rows, cols,
  navbars, etc. Intended to be used with the html5 package. Learn more at 
  <https://getbootstrap.com/>.
	"""
	
	cran = "bsTools" 

	version("1.0.5", md5="51779c68cbb4f538517d8e8e73120517")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-html5@1:", type=("build", "run"))
	depends_on("r-toolbox", type=("build", "run"))
