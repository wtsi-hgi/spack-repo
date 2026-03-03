# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginGlpk(RPackage):
	"""'ROI' Plug-in 'GLPK'

	Enhances the 'R' Optimization Infrastructure ('ROI') package by registering
	     the free 'GLPK' solver. It allows for solving mixed integer linear programming ('MILP')
	     problems as well as all variants/combinations of 'LP', 'IP'.
	"""
	
	homepage = "http://roi.r-forge.r-project.org/"
	cran = "ROI.plugin.glpk" 

	version("1.0-0", md5="c19e183a7a243cdc8e40ba5e163ccf73")

	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-rglpk@0.6.2:", type=("build", "run"))
