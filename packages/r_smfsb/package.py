# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmfsb(RPackage):
	"""Stochastic Modelling for Systems Biology

	Code and data for modelling and simulation of stochastic kinetic biochemical network models. It contains the code and data associated with the second and third editions of the book Stochastic Modelling for Systems Biology, published by Chapman & Hall/CRC Press.
	"""
	
	cran = "smfsb" 

	version("1.5", md5="c212f504f26288f85697d73329169257")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-abind@1.3:", type=("build", "run"))
