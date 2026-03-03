# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivgeo(RPackage):
	"""Basu-Dhar Bivariate Geometric Distribution

	Computes the joint probability mass function (pmf), the joint cumulative function (cdf), the joint survival function (sf), the correlation coefficient, the covariance, the cross-factorial moment and generate random deviates for the Basu-Dhar bivariate geometric distribution as well the joint probability mass, cumulative and survival function assuming the presence of a cure fraction given by the standard bivariate mixture cure fraction model. The package also computes the estimators based on the method of moments.
	"""
	
	homepage = "For"
	cran = "BivGeo" 

	version("2.0.1", md5="97933d308ab942c07033f152508ce491")

	depends_on("r@3.0.2:", type=("build", "run"))
