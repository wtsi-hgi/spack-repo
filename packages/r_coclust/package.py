# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoclust(RPackage):
	"""Copula Based Cluster Analysis

	A copula based clustering algorithm that finds clusters according to the complex multivariate dependence structure of the data generating process. The updated version of the algorithm is described in Di Lascio, F.M.L. and Giannerini, S. (2016). "Clustering dependent observations with copula functions". Statistical Papers, p.1-17. <doi:10.1007/s00362-016-0822-3>.
	"""
	
	cran = "CoClust" 

	version("0.3-2", md5="fe853d36a3a847e20f89953acde99b6b")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
