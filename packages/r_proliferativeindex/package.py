# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProliferativeindex(RPackage):
	"""Calculates and Analyzes the Proliferative Index

	Provides functions for calculating and analyzing the proliferative 
    index (PI) from an RNA-seq dataset. As described in Ramaker & Lasseigne, 
    et al. bioRxiv, 2016 <doi:10.1101/063057>.
	"""
	
	cran = "ProliferativeIndex" 

	version("1.0.1", md5="37cba4aa2bd36302e7a9565774551284")

	depends_on("r@3:", type=("build", "run"))
