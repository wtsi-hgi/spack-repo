# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutreg(RPackage):
	"""Regression Table for Publication

	Create regression tables for publication.
    Currently supports 'lm', 'glm', 'survreg', and 'ivreg' outputs.
	"""
	
	homepage = "https://github.com/kota7/outreg"
	cran = "outreg" 

	version("0.2.2", md5="c2ef756221f0e32b251a7dcfc9087758")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
