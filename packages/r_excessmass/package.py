# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcessmass(RPackage):
	"""Excess Mass Calculation and Plots

	Implementation of a function which calculates the empirical excess mass 
	for given eqn{lambda} and given maximal number of modes (excessm()). Offering 
	powerful plot features to visualize empirical excess mass (exmplot()). This 
	includes the possibility of drawing several plots (with different maximal 
	number of modes / cut off values) in a single graph.
	"""
	
	cran = "ExcessMass" 

	version("1.0.1", md5="416088a41ef34832a3b53ec26ab2198c")

