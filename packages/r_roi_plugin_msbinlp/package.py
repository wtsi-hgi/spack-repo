# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginMsbinlp(RPackage):
	"""'Multi-Solution' Binary Linear Problem Plug-in for the 'R'
Optimization Interface

	Enhances the 'R' Optimization Infrastructure ('ROI') package
             with the possibility to obtain multiple solutions for linear 
             problems with binary variables. The main function is copied 
             (with small modifications) from the relations package.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.msbinlp" 

	version("1.0-1", md5="5a33ae7f9f278e456e71fcf004034f8e")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
