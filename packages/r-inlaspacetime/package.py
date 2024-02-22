# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlaspacetime(RPackage):
	"""Spatial and Spatio-Temporal Models using 'INLA'

	Prepare objects to implement models over spatial and 
  spacetime domains with the 'INLA' package (<https://www.r-inla.org>).
  These objects contain data to for the 'cgeneric' interface in
  'INLA', enabling fast parallel computations.
  We implemented the spatial barrier model, see Bakka et. al. (2019) 
  <doi:10.1016/j.spasta.2019.01.002>, and some of the spatio-temporal 
  models in Lindgren et. al. (2023) <arXiv:2006.04917>. 
  Details are provided in the available vignettes and from the URL bellow.
	"""
	
	homepage = "https://github.com/eliaskrainski/INLAspacetime"
	cran = "INLAspacetime" 

	version("0.1.7", md5="ba616cabf616f6326f55fb0c887c99e3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-fmesher", type=("build", "run"))
