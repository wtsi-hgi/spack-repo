# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecondition(RPackage):
	"""Lightweight Precondition, Postcondition, and Sanity Checks

	Implements fast, safe, and customizable assertions routines, which 
    can be used in place of base::stopifnot(). 
	"""
	
	cran = "precondition" 

	version("0.1.0", md5="50db9fd49a8b910f5f001a9162c2149e")

	depends_on("r-rlang@1.0.6:", type=("build", "run"))
