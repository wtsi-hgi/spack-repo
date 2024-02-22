# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgm(RPackage):
	"""Holonomic Gradient Method and Gradient Descent

	The holonomic gradient method (HGM, hgm) gives a way to evaluate normalization
  constants of unnormalized probability distributions by utilizing holonomic 
  systems of differential or difference equations. The holonomic gradient descent (HGD, hgd) gives a method
  to find maximal likelihood estimates by utilizing the HGM.
	"""
	
	homepage = "http://www.openxm.org"
	cran = "hgm" 

	version("1.23", md5="02e9dd05d931ea00f69a050718aa9c53")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
