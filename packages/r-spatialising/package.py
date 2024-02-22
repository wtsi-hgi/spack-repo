# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialising(RPackage):
	"""Ising Model for Spatial Data

	Performs simulations of binary spatial raster data using
    the Ising model (Ising (1925) <doi:10.1007/BF02980577>; 
    Onsager (1944) <doi:10.1103/PhysRev.65.117>). It allows to set a few
    parameters that represent internal and external pressures, and the number 
    of simulations (Stepinski and Nowosad (2023) <doi:10.1098/rsos.231005>).
	"""
	
	homepage = "https://github.com/Nowosad/spatialising"
	cran = "spatialising" 

	version("0.6.0", md5="f956de2c393d8104e6e9086969824e22")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-comat", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
