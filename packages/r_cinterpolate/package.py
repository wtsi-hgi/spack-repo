# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinterpolate(RPackage):
	"""Interpolation From C

	Simple interpolation methods designed to be used from C
    code. Supports constant, linear and spline interpolation. An R
    wrapper is included but this package is primarily designed to be
    used from C code using 'LinkingTo'.  The spline calculations are
    classical cubic interpolation, e.g., Forsythe, Malcolm and Moler
    (1977) <ISBN: 9780131653320>.
	"""
	
	homepage = "https://github.com/mrc-ide/cinterpolate"
	cran = "cinterpolate" 

	version("1.0.1", md5="f93b24e85504565308a2bbae0f5a1a88")

