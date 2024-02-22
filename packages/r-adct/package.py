# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdct(RPackage):
	"""Adaptive Design in Clinical Trials

	Existing adaptive design methods in clinical trials. The package
    includes power, stopping boundaries (sample size) calculation functions for
    two-group group sequential designs, adaptive design with coprimary endpoints,
    biomarker-informed adaptive design, etc.
	"""
	
	cran = "ADCT" 

	version("0.1.0", md5="dc7d94a01dcc5144bde4cb59825cf6ef")

	depends_on("r-mvtnorm", type=("build", "run"))
