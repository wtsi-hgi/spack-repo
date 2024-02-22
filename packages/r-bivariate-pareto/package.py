# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivariatePareto(RPackage):
	"""Bivariate Pareto Models

	Perform competing risks analysis under bivariate Pareto models. See Shih et al. (2019) <doi:10.1080/03610926.2018.1425450> for details.
	"""
	
	cran = "Bivariate.Pareto" 

	version("1.0.3", md5="3582de8c75f27ac733d3ae8fe01530cd")

	depends_on("r-compound-cox", type=("build", "run"))
