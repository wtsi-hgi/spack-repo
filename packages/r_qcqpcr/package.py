# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcqpcr(RPackage):
	"""Histone ChIP-Seq qPCR Analyzer

	Quality control of chromatin immunoprecipitation libraries (ChIP-seq) by quantitative polymerase chain reaction (qPCR). This function calculates Enrichment value with respect to reference for each histone modification (specific to 'Vii7' software <http://www.thermofisher.com/ca/en/home/life-science/pcr/real-time-pcr/real-time-pcr-instruments/viia-7-real-time-pcr-system/viia-7-software.html>). This function is applicable to full panel of histone modifications described by International Human Epigenomic Consortium (IHEC).
	"""
	
	cran = "qcQpcr" 

	version("1.5", md5="3bdf2fe0412fe0ae3186b41fb801e84e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
