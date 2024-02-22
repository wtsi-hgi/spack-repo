# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiModelsMiplib(RPackage):
	"""'ROI' Access to 'MIPLIB' 2010 Benchmark Instances

	The mixed integer programming library 'MIPLIB' (see <http://miplib.zib.de/>) 
	is commonly used to compare the performance of mixed integer optimization solvers.
	This package provides functions to access 'MIPLIB' from the 
	'R' Optimization Infrastructure ('ROI'). More information about 'MIPLIB'
	can be found in the paper by Koch et al. available at
	<http://mpc.zib.de/index.php/MPC/article/viewFile/56/28>.
	The 'README.md' file illustrates how to use this package.
	"""
	
	homepage = "http://R-Forge.R-project.org/projects/roi"
	cran = "ROI.models.miplib" 

	version("1.0-0", md5="1fbe061ff78cd20373c45e9b8d2b08a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-roi@0.3.0:", type=("build", "run"))
