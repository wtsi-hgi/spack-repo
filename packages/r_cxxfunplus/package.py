# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCxxfunplus(RPackage):
	"""Extend 'cxxfunction' by Saving the Dynamic Shared Objects

	Extend 'cxxfunction' by saving the dynamic shared objects
        for reusing across R sessions.
	"""
	
	homepage = "https://github.com/maverickg/cxxfunplus"
	cran = "cxxfunplus" 

	version("1.0.2", md5="391986b22956cb5b801c513f97d9651e")

	depends_on("r-inline", type=("build", "run"))
