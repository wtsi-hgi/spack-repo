# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginIpop(RPackage):
	"""'ipop' Plug-in for the 'R' Optimization Interface

	Enhances the 'R' Optimization Infrastructure ('ROI') package 
    by registering the 'ipop' solver from package 'kernlab'.
	"""
	
	homepage = "http://roi.r-forge.r-project.org/"
	cran = "ROI.plugin.ipop" 

	version("1.0-0", md5="579a786b7eea54f78f977b0932c6103c")

	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
