# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimcheck(RPackage):
	"""Graphical and Numerical Checks for Mode-Finding Routines

	Tools for checking that the output of an optimization algorithm is indeed at a local mode of the objective function.  This is accomplished graphically by calculating all one-dimensional "projection plots" of the objective function, i.e., varying each input variable one at a time with all other elements of the potential solution being fixed.  The numerical values in these plots can be readily extracted for the purpose of automated and systematic unit-testing of optimization routines.  
	"""
	
	homepage = "https://github.com/mlysy/optimCheck"
	cran = "optimCheck" 

	version("1.0", md5="542f755528c4f4eb8711a1c79a74110b")

