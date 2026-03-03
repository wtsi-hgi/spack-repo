# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapportools(RPackage):
	"""Miscellaneous (Stats) Helper Functions with Sane Defaults for
Reporting

	Helper functions that act as wrappers to more advanced statistical
    methods with the advantage of having sane defaults for quick reporting.
	"""
	
	cran = "rapportools" 

	version("1.1", md5="da08a2a0ba4d06833829dae894e3c6ee")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
