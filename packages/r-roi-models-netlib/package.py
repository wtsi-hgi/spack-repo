# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiModelsNetlib(RPackage):
	"""'ROI' Optimization Problems Based on 'NETLIB-LP'

	A collection of 'ROI' optimization problems based on the 'NETLIB-LP' collection.
  'Netlib' is a software repository, which amongst many other software for scientific computing contains a collection of linear programming problems. The purpose of this package is to make 
  this problems easily accessible from 'R' as 'ROI' optimization problems.
	"""
	
	cran = "ROI.models.netlib" 

	version("1.1-2", md5="2fe254e2c8f9f57fb1aa239e53862368")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
