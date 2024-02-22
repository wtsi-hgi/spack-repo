# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgewis(RPackage):
	"""Tests for Genetic Association/Gene-Environment Interaction in
Longitudinal Studies

	Functions for genome-wide association studies (GWAS)/gene-environment-wide interaction studies (GEWIS) with longitudinal outcomes and exposures. He et al. (2017) "Set-Based Tests for Gene-Environment Interaction in Longitudinal Studies" and He et al. (2017) "Rare-variant association tests in longitudinal studies, with an application to the Multi-Ethnic Study of Atherosclerosis (MESA)".
	"""
	
	cran = "LGEWIS" 

	version("1.1", md5="a641f67c43096f02ccd6c814e47b8d59")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-geem", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
