# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnem(RPackage):
	"""EM Algorithm for Multivariate Skew-Normal Distribution with
Overparametrization

	Efficient estimation of multivariate skew-normal distribution in closed form.
	"""
	
	cran = "snem" 

	version("0.1.1", md5="17a8da61bc1d6be7fdfa5384acaa638b")

	depends_on("r-mvtnorm", type=("build", "run"))
