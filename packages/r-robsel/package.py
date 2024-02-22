# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobsel(RPackage):
	"""Robust Selection Algorithm

	An implementation of algorithms for estimation of the graphical lasso regularization parameter described in Pedro Cisneros-Velarde, Alexander Petersen and Sang-Yun Oh (2020) <http://proceedings.mlr.press/v108/cisneros20a.html>.
	"""
	
	cran = "robsel" 

	version("0.1.0", md5="aa3070529d7ad339f1b7de02a2f197db")

	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
