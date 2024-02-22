# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssetpricing(RPackage):
	"""Optimal Pricing of Assets with Fixed Expiry Date

	Calculates the optimal price of assets (such as
	airline flight seats, hotel room bookings) whose value
	becomes zero after a fixed ``expiry date''.  Assumes
	potential customers arrive (possibly in groups) according
	to a known inhomogeneous Poisson process.  Also assumes a
	known time-varying elasticity of demand (price sensitivity)
	function.  Uses elementary techniques based on ordinary
	differential equations.  Uses the package deSolve to effect
	the solution of these differential equations.
	"""
	
	homepage = "http://www.stat.auckland.ac.nz/~rolf/"
	cran = "AssetPricing" 

	version("1.0-3", md5="1bc9259745f2863b359c4b3608bb827a")

	depends_on("r@0.99:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
