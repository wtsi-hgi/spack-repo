# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbpower(RPackage):
	"""Finite Sample Power Calculations for Detection Boundary Tests

	Calculates lower bound on power, upper bound on power, and exact power (small sets only) for detection boundary tests (e.g. Berk-Jones, Generalized Berk-Jones, innovated Berk-Jones) used in set-based inference studies. These detection boundary tests are described in Sun et al., (2019) <doi:10.1080/01621459.2019.1660170>.
	"""
	
	cran = "DBpower" 

	version("0.1.0", md5="2a12a1273daafde062bc69481520b608")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-gbj", type=("build", "run"))
	depends_on("r-kit", type=("build", "run"))
