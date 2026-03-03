# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunr(RPackage):
	"""Simple Utility Providing Terminal Access to all R Functions

	A small utility which wraps Rscript and provides access to all R
    functions from the shell.
	"""
	
	homepage = "https://github.com/sahilseth/funr"
	cran = "funr" 

	version("0.3.2", md5="4c672fc909d18a7e64315cf1d71b9109")

