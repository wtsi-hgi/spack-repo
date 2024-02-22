# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbsmodelling(RPackage):
	"""GUI Tools Made Easy: Interact with Models and Explore Data

	Provides software to facilitate the design, testing, and operation
   of computer models. It focuses particularly on tools that make it easy to
   construct and edit a customized graphical user interface ('GUI'). Although our
   simplified 'GUI' language depends heavily on the R interface to the 'Tcl/Tk'
   package, a user does not need to know 'Tcl/Tk'. Examples illustrate models
   built with other R packages, including 'PBSmapping', 'PBSddesolve', and 'BRugs'. 
   A complete user's guide 'PBSmodelling-UG.pdf' shows how to use this package
   effectively.
	"""
	
	homepage = "https://github.com/pbs-software/pbs-modelling"
	cran = "PBSmodelling" 

	version("2.69.3", md5="f4d9ece3945c750fb622f0192c1bc1e1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
