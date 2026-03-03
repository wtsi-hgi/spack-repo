# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbhdesign(RPackage):
	"""Spatial Designs for Ecological and Environmental Surveys

	Provides spatially survey balanced designs using the quasi-random number method described Robinson et al. (2013) <doi:10.1111/biom.12059> and adjusted in Robinson et al. (2017) <doi:10.1016/j.spl.2017.05.004>. Designs using MBHdesign can: 1) accommodate, without substantial detrimental effects on spatial balance, legacy sites (Foster et al., 2017 <doi:10.1111/2041-210X.12782>); 2) be based on points or transects (foster et al. 2020 <doi:10.1111/2041-210X.13321> and produce clustered samples (Foster et al. (in press). Additional information about the package use itself is given in Foster (2021) <doi:10.1111/2041-210X.13535>.
	"""
	
	cran = "MBHdesign" 

	version("2.3.15", md5="0493eeba3ac93333ed5eff9be0100bc0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
