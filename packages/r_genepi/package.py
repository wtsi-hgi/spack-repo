# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenepi(RPackage):
	"""Genetic Epidemiology Design and Inference

	Package for Genetic Epidemiologic Methods Developed at MSKCC. It contains functions to calculate haplotype specific odds ratio and the power of two stage design for GWAS studies. 
	"""
	
	cran = "genepi" 

	version("1.0.3", md5="fddebe2ef40d474e9108ddd57d57597d")

	depends_on("r@2:", type=("build", "run"))
