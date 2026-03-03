# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormpsy(RPackage):
	"""Normalisation of Psychometric Tests

	Functions for normalizing psychometric test scores. The normalization aims at correcting the metrological properties of the psychometric tests such as the ceiling and floor effects and the curvilinearity (unequal interval scaling). Functions to compute and plot predictions in the natural scale of the psychometric test from the estimates of a linear mixed model estimated on the normalized scores are also provided. See Philipps et al (2014) <doi:10.1159/000365637> for details.
	"""
	
	cran = "NormPsy" 

	version("1.0.8", md5="f2545b6a69478b1829f421a498fadb60")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lcmm@1.7.1:", type=("build", "run"))
