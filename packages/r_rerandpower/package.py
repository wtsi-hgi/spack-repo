# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRerandpower(RPackage):
	"""Power and Sample Size Calculations for Completely Randomized and
Rerandomized Experiments

	Computes the power resulting from completely randomized and rerandomized experiments with two groups. Furthermore, computes the sample size necessary to obtain a desired level of power for completely randomized and rerandomized experiments.
	"""
	
	cran = "rerandPower" 

	version("0.0.1", md5="02b9f667160c00579a91cbd5b286502a")

	depends_on("r-runuran", type=("build", "run"))
