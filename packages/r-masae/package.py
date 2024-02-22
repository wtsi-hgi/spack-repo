# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMasae(RPackage):
	"""Mandallaz' Model-Assisted Small Area Estimators

	An S4 implementation of the unbiased extension of
    the model- assisted synthetic-regression estimator proposed by
    Mandallaz (2013) <DOI:10.1139/cjfr-2012-0381>, Mandallaz et al. (2013)
    <DOI:10.1139/cjfr-2013-0181> and Mandallaz (2014)
    <DOI:10.1139/cjfr-2013-0449>.  It yields smaller variances than the
    standard bias correction, the generalised regression estimator.
	"""
	
	homepage = "https://gitlab.com/fvafrCU/maSAE"
	cran = "maSAE" 

	version("2.0.3", md5="db89f7c3a618146d50022480aa60eb26")

	depends_on("r@3.6:", type=("build", "run"))
