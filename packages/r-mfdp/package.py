# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfdp(RPackage):
	"""Flexible Control of the mFDP

	Computes bounds for the median of the false discovery proportion (mFDP).
	These 50 percent confidence bounds for the FDP are simultaneously valid. 
	The method takes a vector of p-values as input. Also provides mFDP-adjusted p-values. 
	Can be used for flexible mFDP control.
	"""
	
	cran = "mFDP" 

	version("0.1.0", md5="9a4cc025b9d7077194f8ec2342545008")

