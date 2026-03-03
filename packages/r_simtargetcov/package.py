# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtargetcov(RPackage):
	"""Data Transformation or Simulation with Empirical Covariance
Matrix

	Transforms or simulates data with a target empirical covariance matrix supplied
             by the user. The method to obtain the data with the target empirical covariance
             matrix is described in Section 5.1 of Christidis, Van Aelst and Zamar (2019)
             <arXiv:1812.05678>.
	"""
	
	cran = "simTargetCov" 

	version("1.0.1", md5="ba15296f8deb8dc47f8bc9c938800642")

	depends_on("r-mass", type=("build", "run"))
