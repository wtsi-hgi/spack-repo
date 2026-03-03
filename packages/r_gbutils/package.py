# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbutils(RPackage):
	"""Utilities for Simulation, Plots, Quantile Functions and
Programming

	Plot density and distribution functions with automatic selection of
       suitable regions. Numerically invert (compute quantiles) distribution
       functions. Simulate real and complex numbers from distributions of their
       magnitude and arguments. Optionally, the magnitudes and/or arguments may
       be fixed in almost arbitrary ways. Create polynomials from roots given in
       Cartesian or polar form. Small programming utilities: check if an object
       is identical to NA, count positional arguments in a call, set
       intersection of more than two sets, check if an argument is unnamed,
       compute the graph of S4 classes in packages.
	"""
	
	homepage = "https://github.com/GeoBosh/gbutils"
	cran = "gbutils" 

	version("0.5", md5="22648ff70cf990fd3f01f4a6a59f229f")

	depends_on("r-rdpack@0.9:", type=("build", "run"))
