# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoet(RPackage):
	"""Principal Orthogonal ComplEment Thresholding (POET) Method

	Estimate large covariance matrices in approximate factor
        models by thresholding principal orthogonal complements.
	"""
	
	cran = "POET" 

	version("2.0", md5="e6b63d282200f515dd140e17615622b3")

