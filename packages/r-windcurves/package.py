# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWindcurves(RPackage):
	"""Tool to Fit Wind Turbine Power Curves

	Provides a tool to fit and compare the wind turbine power curves 
    with successful curve fitting techniques. Facilitates to examine and compare 
    the performance of a user-defined power curve fitting techniques. 
    Also, provide features to generate power curve discrete points from a graphical 
    power curves. Data on the power curves of the wind turbine from major 
    manufacturers are provided.
	"""
	
	homepage = "https://www.neerajbokde.in/viggnette/2021-10-14-WindCurves/"
	cran = "WindCurves" 

	version("0.2", md5="a3dc5a08e5d8961b74b2c00a0ce30d26")

	depends_on("r-readbitmap", type=("build", "run"))
