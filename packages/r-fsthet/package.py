# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsthet(RPackage):
	"""Fst-Heterozygosity Smoothed Quantiles

	A program to generate smoothed quantiles for the Fst-heterozygosity distribution. Designed for use with large numbers of loci (e.g., genome-wide SNPs). The best case for analyzing the Fst-heterozygosity distribution is when many populations (>10) have been sampled. See Flanagan & Jones (2017) <doi:10.1093/jhered/esx048>.
	"""
	
	cran = "fsthet" 

	version("1.0.1", md5="f76872a25f740c0a15b062b28f47faa3")

	depends_on("r@2.10:", type=("build", "run"))
