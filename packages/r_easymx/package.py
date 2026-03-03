# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasymx(RPackage):
	"""Easy Model-Builder Functions for 'OpenMx'

	Utilities for building certain kinds of common matrices and models in 
    the extended structural equation modeling package, 'OpenMx'.
	"""
	
	homepage = "https://bitbucket.org/mhunter/easymx"
	cran = "EasyMx" 

	version("0.3-2", md5="3c9099f574f26d78e2dbd8087518a8be")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
