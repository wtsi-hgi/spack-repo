# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNspmix(RPackage):
	"""Nonparametric and Semiparametric Mixture Estimation

	Mainly for maximum likelihood estimation of nonparametric
             and semiparametric mixture models, but can also be used
             for fitting finite mixtures. The algorithms are
             developed in Wang (2007)
             <doi:10.1111/j.1467-9868.2007.00583.x> and Wang (2010)
             <doi:10.1007/s11222-009-9117-z>.
	"""
	
	homepage = "https://www.stat.auckland.ac.nz/~yongwang/"
	cran = "nspmix" 

	version("1.5-0", md5="f4e98de134b7fba199154984f5592606")

	depends_on("r-lsei", type=("build", "run"))
