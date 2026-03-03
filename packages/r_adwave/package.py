# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdwave(RPackage):
	"""Wavelet Analysis of Genomic Data from Admixed Populations

	Implements wavelet-based approaches for describing population admixture. Principal Components Analysis (PCA) is used to define the population structure and produce a localized admixture signal for each individual. Wavelet summaries of the PCA output describe variation present in the data and can be related to population-level demographic processes. For more details, see J Sanderson, H Sudoyo, TM Karafet, MF Hammer and MP Cox. 2015. Reconstructing past admixture processes from local genomic ancestry using wavelet transformation. Genetics 200:469-481 <doi:10.1534/genetics.115.176842>.
	"""
	
	homepage = "https://doi.org/10.1534/genetics.115.176842"
	cran = "adwave" 

	version("1.3", md5="5ce79cf19a1a98364281866889039965")

	depends_on("r-waveslim", type=("build", "run"))
