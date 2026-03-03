# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgof(RPackage):
	"""Discrete Goodness-of-Fit Tests

	A revision to the stats::ks.test() function and the associated
        ks.test.Rd help page. With one minor exception, it does not change the
        existing behavior of ks.test(), and it adds features necessary
        for doing one-sample tests with hypothesized discrete
        distributions. The package also contains cvm.test(), for doing
        one-sample Cramer-von Mises goodness-of-fit tests.
	"""
	
	cran = "dgof" 

	version("1.4", md5="d1fd678118c39e29637a68bf298e6e72")

