# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmony(RPackage):
	"""Fast, Sensitive, and Accurate Integration of Single Cell Data

	Implementation of the Harmony algorithm for single cell integration, described in Korsunsky et al <doi:10.1038/s41592-019-0619-0>. Package includes a standalone Harmony function and interfaces to external frameworks.
	"""
	
	homepage = "software.broadinstitute.org/harmony"
	cran = "harmony" 

	version("1.2.0", md5="4c40181d0401b1e3e6350d40806b08ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
