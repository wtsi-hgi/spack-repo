# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaumbrella(RPackage):
	"""Umbrella Review Package for R

	A comprehensive range of facilities to perform umbrella reviews with stratification of the evidence in R. The package accomplishes this aim by building on three core functions that: (i) automatically perform all required calculations in an umbrella review (including but not limited to meta-analyses), (ii) stratify evidence according to various classification criteria, and (iii) generate a visual representation of the results. Note that if you are not familiar with R, the core features of this package are available from a web browser (<https://www.metaumbrella.org/>).
	"""
	
	cran = "metaumbrella" 

	version("1.0.11", md5="5ee2419f5fb610da1762621e12726866")
	version("1.0.10", md5="f5a428c3deeb031748b00c8d49de1955")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-powersurvepi", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
