# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGargoyle(RPackage):
	"""An Event-Based Mechanism for 'Shiny'

	An event-Based framework for building 'Shiny' apps.
    Instead of relying on standard 'Shiny' reactive objects, this 
    package allow to relying on a lighter set of triggers, so that 
    reactive contexts can be invalidated with more control.
	"""
	
	cran = "gargoyle" 

	version("0.0.1", md5="9161c80e6b189914d6d55cae079c832b")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
