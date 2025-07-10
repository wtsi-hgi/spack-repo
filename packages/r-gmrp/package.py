# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmrp(RPackage):
	"""GWAS-based Mendelian Randomization and Path Analyses

	Perform Mendelian randomization analysis of multiple SNPs to determine risk factors causing disease of study and to exclude confounding variabels and perform path analysis to construct path of risk factors to the disease.
	"""
	
	bioc = "GMRP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GMRP_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GMRP/GMRP_1.30.0.tar.gz"]

	version("1.30.0", sha256="a97f451eaf5e2f79c6655710e55cc057a3b209b103d18eaf4757b54d45f6a495")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
