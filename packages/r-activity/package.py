# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivity(RPackage):
	"""Animal Activity Statistics

	Provides functions to express clock time data relative to 
    anchor points (typically solar); fit kernel density functions to animal 
    activity time data; plot activity distributions; quantify overall 
    levels of activity; statistically compare activity metrics through 
    bootstrapping; evaluate variation in linear variables with time (or 
    other circular variables).
	"""
	
	cran = "activity" 

	version("1.3.4", md5="9957a7368285c1a0438094f319ca2db3")

	depends_on("r-pbapply", type=("build", "run"))
