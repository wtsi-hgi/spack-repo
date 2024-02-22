# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnm(RPackage):
	"""Multivariate Nonparametric Methods. An Approach Based on Spatial
Signs and Ranks

	Multivariate tests, estimates and methods based on the identity score, spatial sign score and spatial rank score are provided. The methods include one and c-sample problems, shape estimation and testing, linear regression and principal components. The methodology is described in Oja (2010) <doi:10.1007/978-1-4419-0468-3> and Nordhausen and Oja (2011) <doi:10.18637/jss.v043.i05>.  
	"""
	
	cran = "MNM" 

	version("1.0-4", md5="69d6f3d533ede224bbbe81f8baf6d6f9")

	depends_on("r@2.9.2:", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-spatialnp", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-ics", type=("build", "run"))
