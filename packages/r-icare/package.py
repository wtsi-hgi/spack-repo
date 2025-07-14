# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcare(RPackage):
	"""A Tool for Individualized Coherent Absolute Risk Estimation (iCARE)

	An R package to compute Individualized Coherent Absolute Risk Estimators.
	"""
	
	bioc = "iCARE"

	version("1.36.0", commit="94da641c3e1cb2bde4a36f98aeaadb1a146bae0b")
	version("1.30.0", commit="4a58d84f51a45df07a226baeb063b9ae70dfc1b7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
