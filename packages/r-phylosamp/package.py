# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylosamp(RPackage):
	"""Sample Size Calculations for Molecular and Phylogenetic Studies

	Implements novel tools for estimating sample sizes needed for phylogenetic studies, including
    studies focused on estimating the probability of true pathogen transmission between two cases given phylogenetic linkage and studies focused on tracking pathogen variants at a population level. Methods described in Wohl, Giles, and Lessler (2021) and in Wohl, Lee, DiPrete, and Lessler (2023).
	"""
	
	homepage = "https://github.com/HopkinsIDD/phylosamp"
	cran = "phylosamp" 

	version("1.0.1", md5="c6b6af53fd40f08220366b8c8ccc9369")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
