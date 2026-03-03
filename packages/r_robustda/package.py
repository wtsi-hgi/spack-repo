# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustda(RPackage):
	"""Robust Mixture Discriminant Analysis

	Robust mixture discriminant analysis (RMDA), proposed in Bouveyron & Girard, 2009 <doi:10.1016/j.patcog.2009.03.027>, allows to build a robust supervised classifier from learning data with label noise. The idea of the proposed method is to confront an unsupervised modeling of the data with the supervised information carried by the labels of the learning data in order to detect inconsistencies. The method is able afterward to build a robust classifier taking into account the detected inconsistencies into the labels.
	"""
	
	cran = "robustDA" 

	version("1.2", md5="54a56da7ce572a92d61ddf41c7974cde")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
