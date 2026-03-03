# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpaero(RPackage):
	"""Software for Project AERO

	Implements methods for anticipating the emergence and eradication
    of infectious diseases from surveillance time series. Also provides support
    for computational experiments testing the performance of such methods.
	"""
	
	cran = "spaero" 

	version("0.6.0", md5="96b2dc163c935be75fc5b31c98dd6d09")

	depends_on("r@3.2.1:", type=("build", "run"))
