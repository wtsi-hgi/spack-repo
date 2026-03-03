# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissplot(RPackage):
	"""Missing Plot Technique in Design of Experiment

	A system for testing differential effects among treatments in case of Randomised Block Design and Latin Square Design when there is one missing observation. Methods for this process are as described in A.M.Gun,M.K.Gupta and B.Dasgupta(2019,ISBN:81-87567-81-3). 
	"""
	
	cran = "Missplot" 

	version("0.1.0", md5="238a158f0f6d0400ef8335a1596ad0dc")

