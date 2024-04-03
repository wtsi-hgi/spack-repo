# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfcons(RPackage):
	"""Confidence and Consistency of Predictive Distribution Models

	Calculate confidence and consistency that measure the
    goodness-of-fit and transferability of predictive/potential distribution
    models (including species distribution models) as described by Somodi &
    Bede-Fazekas et al. (2024) <doi:10.1016/j.ecolmodel.2024.110667>.
	"""
	
	homepage = "https://github.com/bfakos/confcons"
	cran = "confcons" 

	version("0.3.1", md5="fccd7cb765892db3c7e712d5020a4e0d")

