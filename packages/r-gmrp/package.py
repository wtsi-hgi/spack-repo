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

	version("1.36.0", commit="120e8c19cf30cf06615c56a8da2091763589fefb")
	version("1.30.0", commit="5b446069132e2f180d48cc293eb35456de12349a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
