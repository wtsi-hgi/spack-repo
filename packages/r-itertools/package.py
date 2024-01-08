# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RItertools(RPackage):
	"""Iterator Tools

	Various tools for creating iterators, many patterned after
        functions in the Python itertools module, and others patterned
        after functions in the 'snow' package.
	"""
	
	cran = "itertools" 

	version("0.1-3", md5="c9bafb575b42a663da47739e04e79105")

	depends_on("r@2.14.0:", type=("build", "run"))
	depends_on("r-iterators@1.0.0:", type=("build", "run"))
