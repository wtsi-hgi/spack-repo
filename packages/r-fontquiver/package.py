# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RFontquiver(RPackage):
	"""Set of Installed Fonts

	Provides a set of fonts with permissive licences. This is
    useful when you want to avoid system fonts to make sure your
    outputs are reproducible.
	"""
	
	cran = "fontquiver" 

	version("0.2.1", md5="eddbde07ef14475acfbdc9e82d45385a")

	depends_on("r@3.0.0:", type=("build", "run"))
	depends_on("r-fontbitstreamvera@0.1.0:", type=("build", "run"))
	depends_on("r-fontliberation@0.1.0:", type=("build", "run"))
