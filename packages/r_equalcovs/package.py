# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REqualcovs(RPackage):
	"""Testing the Equality of Two Covariance Matrices

	Tests the equality of two covariance matrices, used in paper "Two sample tests for high dimensional covariance matrices." Li and Chen (2012) <arXiv:1206.0917>.
	"""
	
	cran = "equalCovs" 

	version("1.0", md5="1a8d664e1a6dbccce126881830ae5b2b")

