# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoregressionmde(RPackage):
	"""Minimum Distance Estimation in Autoregressive Model

	Consider autoregressive model of order p where the distribution function of innovation is unknown, but innovations are independent and symmetrically distributed. The package contains a function named ARMDE which takes X (vector of n observations) and p (order of the model) as input argument and returns minimum distance estimator of the parameters in the model.
	"""
	
	cran = "AutoregressionMDE" 

	version("1.0", md5="c9767fbfaba4dfc5a8b72f0af956c4f8")

	depends_on("r@3.2.2:", type=("build", "run"))
