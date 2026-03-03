# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeawaveq(RPackage):
	"""SEAWAVE-Q Model

	A model and utilities for analyzing trends in chemical concentrations in streams with a seasonal wave (seawave) and adjustment for streamflow (Q) and other ancillary variables. See Ryberg and York, 2020, <doi:10.3133/ofr20201082>.
	"""
	
	homepage = "https://doi.org/10.3133/ofr20201082"
	cran = "seawaveQ" 

	version("2.0.2", md5="3a2ee006b6b02e5d59bf153e1f13a07e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
