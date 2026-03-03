# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllelicseries(RPackage):
	"""Allelic Series Test

	Implementation of gene-level rare variant association tests targeting allelic series: genes where increasingly deleterious mutations have increasingly large phenotypic effects. The COding-variant Allelic Series Test (COAST) operates on the benign missense variants (BMVs), deleterious missense variants (DMVs), and protein truncating variants (PTVs) within a gene. COAST uses a set of adjustable weights that tailor the test towards rejecting the null hypothesis for genes where the average magnitude of effect increases monotonically from BMVs to DMVs to PTVs. See McCaw ZR, O’Dushlaine C, Somineni H, Bereket M, Klein C, Karaletsos T, Casale FP, Koller D, Soare TW. (2022) "An allelic series rare variant association test for candidate gene discovery" <doi:10.1101/2022.12.23.521658>. 
	"""
	
	cran = "AllelicSeries" 

	version("0.0.4.1", md5="e0caddace4164edfbd69de12f2a9baad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rnomni", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
