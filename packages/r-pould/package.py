# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPould(RPackage):
	"""Phased or Unphased Linkage Disequilibrium

	Computes the D', Wn, and conditional asymmetric linkage disequilibrium (ALD) measures for pairs of genetic loci. Performs these linkage disequilibrium (LD) calculations on phased genotype data recorded using Genotype List (GL) String or columnar formats. Alternatively, generates expectation-maximization (EM) estimated haplotypes from phased data, or performs LD calculations on EM estimated haplotypes. Performs sign tests comparing LD values for phased and unphased datasets, and generates heat-maps for each LD measure. Described by Osoegawa et al. (2019a) <doi:10.1016/j.humimm.2019.01.010>, and Osoegawa et. al. (2019b) <doi:10.1016/j.humimm.2019.05.018>.
	"""
	
	cran = "pould" 

	version("1.0.1", md5="16242a8827c20ac9ecf4cf5784e3e61f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-haplo-stats", type=("build", "run"))
	depends_on("r-gap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bigdawg", type=("build", "run"))
