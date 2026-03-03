# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClonality(RPackage):
	"""Clonality testing

	Statistical tests for clonality versus independence of tumors from the same patient based on their LOH or genomewide copy number profiles
	"""
	
	bioc = "Clonality" 

	version("1.50.0", commit="63d4ea324bbb444a66929137e224ad3c2a5040aa")

	depends_on("r@2.12.2:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
