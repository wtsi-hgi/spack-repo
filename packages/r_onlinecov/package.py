# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlinecov(RPackage):
	"""Online Change Point Detection in High-Dimensional Covariance
Structure

	Implement a new stopping rule to detect anomaly in the covariance structure of high-dimensional online data. The detection procedure can be applied to Gaussian or non-Gaussian data with a large number of components. Moreover, it allows both spatial and temporal dependence in data. The dependence can be estimated by a data-driven procedure. The level of threshold in the stopping rule can be determined at a pre-selected average run length. More detail can be seen in Li, L. and Li, J. (2020) "Online Change-Point Detection in High-Dimensional Covariance Structure with Application to Dynamic Networks." <arXiv:1911.07762>.
	"""
	
	cran = "onlineCOV" 

	version("1.3", md5="8b15ac9e587bfdfbb3ad6a47e65632dc")

