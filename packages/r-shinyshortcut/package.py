# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyshortcut(RPackage):
	"""Creates an Executable Shortcut for Shiny Applications

	Provides function shinyShortcut() that, 
    when given the base directory of a shiny application, will produce an
    executable file that runs the shiny app directly in the user's
    default browser. Tested on both windows and unix machines. Inspired
    by and borrowing from 
    <http://www.mango-solutions.com/wp/2017/03/shiny-based-tablet-or-desktop-app/>.
	"""
	
	cran = "shinyShortcut" 

	version("0.1.0", md5="f5d22fa5c563a795aba03a270e30fe0b")

	depends_on("r@3.2.3:", type=("build", "run"))
