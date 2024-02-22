# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteomicscv(RPackage):
	"""Calculates the Percentage CV for Mass Spectrometry-Based
Proteomics Data

	Calculates the percentage coefficient of variation (CV) for mass spectrometry-based proteomic data. Intensity based quantification is log normal, there the CV is calculated with the lognormal function. This package currently does not reference any academic publication.
	"""
	
	cran = "proteomicsCV" 

	version("0.1.0", md5="3bc7536875d114c1b893eb79b1b21ce4")

