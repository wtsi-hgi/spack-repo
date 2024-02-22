# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbdat(RPackage):
	"""Implementation of BDAT Tree Taper Fortran Functions

	Implementing the BDAT tree taper Fortran routines, which were
  developed for the German National Forest Inventory (NFI), to calculate 
  diameters, volume, assortments, double bark thickness and biomass for
  different tree species based on tree characteristics and sorting information.
  See Kublin (2003) <doi:10.1046/j.1439-0337.2003.00183.x> for details.
	"""
	
	homepage = "https://gitlab.com/vochr/rbdat"
	cran = "rBDAT" 

	version("1.0.0", md5="db9ddf5ee30bb955b20292d9061a447a")

