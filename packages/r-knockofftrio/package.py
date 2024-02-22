# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnockofftrio(RPackage):
	"""Trio Data Analysis with Knockoff Statistics for FDR Control

	Identification of putative causal variants in genome-wide association studies with the trio design. The package implements the methods in the paper: Yang, Y., Wang, C., Liu, L., Buxbaum, J., He, Z., & Ionita-Laza, I. (2022). KnockoffTrio: A knockoff framework for the identification of putative causal variants in genome-wide association studies with trio design. The American Journal of Human Genetics, 109(10), 1761-1776.
	"""
	
	cran = "KnockoffTrio" 

	version("1.0.2", md5="2004b439a43c5248c59c31eaea6c5a9b")

	depends_on("r@2.10:", type=("build", "run"))
