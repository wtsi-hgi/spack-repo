# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaliteAe(RPackage):
	"""Adverse Events Analysis Using 'metalite'

	Analyzes adverse events in clinical trials using the 'metalite'
    data structure. The package simplifies the workflow to create
    production-ready tables, listings, and figures discussed in the
    adverse events analysis chapters of
    "R for Clinical Study Reports and Submission"
    by Zhang et al. (2022) <https://r4csr.org/>.
	"""
	
	homepage = "https://merck.github.io/metalite.ae/"
	cran = "metalite.ae" 

	version("0.1.1", md5="237422f5923f595cf4b80d657b7d85ff")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-metalite", type=("build", "run"))
	depends_on("r-r2rtf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
