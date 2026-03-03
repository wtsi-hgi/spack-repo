# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynthacs(RPackage):
	"""Synthetic Microdata and Spatial MicroSimulation Modeling for ACS
Data

	Provides access to curated American Community Survey (ACS) base tables via a wrapper
  to library(acs). Builds synthetic micro-datasets at any user-specified geographic level with
  ten default attributes; and, conducts spatial microsimulation modeling (SMSM) via simulated
  annealing.  SMSM is conducted in parallel by default. Lastly, we provide functionality for
  data-extensibility of micro-datasets <doi:10.18637/jss.v104.i07>.
	"""
	
	cran = "synthACS" 

	version("1.7.1", md5="95f5261275b1e9c527c47fb9cac7c853")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-acs@2.1:", type=("build", "run"))
	depends_on("r-retry", type=("build", "run"))
