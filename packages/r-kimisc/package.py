# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKimisc(RPackage):
	"""Kirill's Miscellaneous Functions

	A collection of useful functions not found anywhere else,
        mainly for programming: Pretty intervals, generalized lagged
        differences, checking containment in an interval, and an
        alternative interface to assign().
	"""
	
	homepage = "http://krlmlr.github.io/kimisc"
	cran = "kimisc" 

	version("0.4", md5="7458c52af0a6d259db6b7e1573850a5a")

	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
