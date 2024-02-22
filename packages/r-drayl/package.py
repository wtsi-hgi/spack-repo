# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrayl(RPackage):
	"""Computation of Rayleigh Densities of Arbitrary Dimension

	We offer an implementation of the series representation put 
  forth in "A series representation for multidimensional 
  Rayleigh distributions" by Wiegand and Nadarajah <DOI: 
  10.1002/dac.3510>. Furthermore we have implemented an 
  integration approach proposed by Beaulieu et al. for 3 and 
  4-dimensional Rayleigh densities (Beaulieu, Zhang,  "New 
  simplest exact forms for the 3D and 4D multivariate Rayleigh 
  PDFs with applications to antenna array geometrics", <DOI: 
  10.1109/TCOMM.2017.2709307>). 
	"""
	
	cran = "DRAYL" 

	version("1.0", md5="a872c014bf9ed030f08d9a97c365f484")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rconics", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
