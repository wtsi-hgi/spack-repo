# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPossa(RPackage):
	"""Power Simulation for Sequential Analyses and Multiple Hypotheses

	Calculates, via simulation, power and appropriate stopping
  alpha boundaries (and/or futility bounds) for sequential analyses (i.e.,
  group sequential design) as well as for multiple hypotheses (multiple tests
  included in an analysis), given any specified global error rate. This enables
  the sequential use of practically any significance test, as long as the
  underlying data can be simulated in advance to a reasonable approximation.
  Lukács (2022) <doi:10.21105/joss.04643>.
	"""
	
	homepage = "https://github.com/gasparl/possa"
	cran = "POSSA" 

	version("0.6.4", md5="e118d4a727d2d4bc3382404049b189c3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
