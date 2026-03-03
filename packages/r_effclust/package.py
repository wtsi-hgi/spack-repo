# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffclust(RPackage):
	"""Calculate Effective Number of Clusters for a Linear Model

	Calculates the (approximate) effective number of clusters for a regression model, as described in Carter, Schnepel, and Steigerwald (2017) <doi:10.1162/REST_a_00639>.  The effective number of clusters is a statistic to assess the reliability of asymptotic inference when sampling or treatment assignment is clustered. Methods are implemented for stats::lm(), plm::plm(), and fixest::feols(). There is also a formula method.
	"""
	
	cran = "effClust" 

	version("0.8.0", md5="6e53b38dee3df6b4b6ace6c72c2e6a11")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
