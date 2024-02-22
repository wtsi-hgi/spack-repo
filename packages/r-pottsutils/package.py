# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPottsutils(RPackage):
	"""Utility Functions of the Potts Models

	There are three sets of functions. The first produces
             basic properties of a graph and generates samples from
             multinomial distributions to facilitate the simulation
	     functions (they maybe used for other purposes as well).
	     The second provides various simulation functions for a
	     Potts model in Potts, R. B. (1952)
	     <doi:10.1017/S0305004100027419>.
	     The third currently includes only one function which
	     computes the normalizing constant of a Potts model
	     based on simulation results.
	"""
	
	cran = "PottsUtils" 

	version("0.3-3", md5="f0168b5048d3bf05920b46dd3db70908")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-miscf@0.1.4:", type=("build", "run"))
