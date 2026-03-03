# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmi(RPackage):
	"""Mutual Information Estimators

	Provides mutual information estimators based on k-nearest neighbor estimators by A. Kraskov, et al. (2004) <doi:10.1103/PhysRevE.69.066138>, S. Gao, et al. (2015) <http://proceedings.mlr.press/v38/gao15.pdf> and local density estimators by W. Gao, et al. (2017) <doi:10.1109/ISIT.2017.8006749>.
	"""
	
	cran = "rmi" 

	version("0.1.1", md5="f50fe756a7049cf2132c209f6a4d68ec")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
