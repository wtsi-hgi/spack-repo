# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwekajars(RPackage):
	"""R/Weka Interface Jars

	External jars required for package 'RWeka'.
	"""
	
	cran = "RWekajars" 

	version("3.9.3-2", md5="dfdbabfb09ff87cbc2570b35ed2534c0")

	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
