# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrim(RPackage):
	"""Patient Rule Induction Method (PRIM)

	Patient Rule Induction Method (PRIM) for bump hunting in high-dimensional data.
	"""
	
	homepage = "https://www.mvstat.net/tduong/"
	cran = "prim" 

	version("1.0.21", md5="92709c98c496c120e8c4c0163769aaa6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
