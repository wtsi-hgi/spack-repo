# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDem(RPackage):
	"""The Distributed EM Algorithms in Multivariate Gaussian Mixture
Models

	The distributed expectation maximization algorithms are used to solve parameters of multivariate Gaussian mixture models. The philosophy of the package is described in Guo, G. (2022) <doi:10.1080/02664763.2022.2053949>.
	"""
	
	cran = "DEM" 

	version("0.0.0.2", md5="8c164f03925547c6dff22e63586c672c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
