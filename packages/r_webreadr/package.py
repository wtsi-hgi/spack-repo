# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebreadr(RPackage):
	"""Tools for Reading Formatted Access Log Files

	R is used by a vast array of people for a vast array of purposes
    - including web analytics. This package contains functions for consuming and
    munging various common forms of request log, including the Common and Combined
    Web Log formats and various Amazon access logs.
	"""
	
	homepage = "https://github.com/Ironholds/webreadr"
	cran = "webreadr" 

	version("0.4.0", md5="16710d05e1b742bd947d5d4b0a36a235")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
