# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPense(RPackage):
	"""Penalized Elastic Net S/MM-Estimator of Regression

	Robust penalized (adaptive) elastic net S and M estimators for
    linear regression. The methods are proposed in
    Cohen Freue, G. V., Kepplinger, D., Salibián-Barrera, M., and Smucler, E.
    (2019) <https://projecteuclid.org/euclid.aoas/1574910036>.
    The package implements the extensions and algorithms described in
    Kepplinger, D. (2020) <doi:10.14288/1.0392915>.
	"""
	
	homepage = "https://dakep.github.io/pense-rpkg/"
	cran = "pense" 

	version("2.2.0", md5="67253bbc968bfd6ef9ce810025de035e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.600:", type=("build", "run"))
