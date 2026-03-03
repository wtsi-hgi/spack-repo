# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBerryfunctions(RPackage):
	"""Function Collection Related to Plotting and Hydrology

	Draw horizontal histograms, color scattered points by 3rd dimension,
    enhance date- and log-axis plots, zoom in X11 graphics, trace errors and warnings, 
    use the unit hydrograph in a linear storage cascade, convert lists to data.frames and arrays, 
    fit multiple functions.
	"""
	
	homepage = "https://github.com/brry/berryFunctions"
	cran = "berryFunctions" 

	version("1.22.5", md5="92ba44152b782881848df66f56e86396")

	depends_on("r-abind", type=("build", "run"))
