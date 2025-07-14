# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrenchfish(RPackage):
	"""Poisson Models for Quantifying DNA Copy-number from FISH Images of Tissue Sections

	FrenchFISH comprises a nuclear volume correction method coupled with two types of Poisson models: either a Poisson model for improved manual spot counting without the need for control probes; or a homogenous Poisson Point Process model for automated spot counting.
	"""
	
	bioc = "frenchFISH" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/frenchFISH_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/frenchFISH/frenchFISH_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="09cc83d7bc246a8b8da57c724237793670032c9223a1248765ed3b121a07e603")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-nhpoisson", type=("build", "run"))
