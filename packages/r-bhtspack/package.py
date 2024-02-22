# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhtspack(RPackage):
	"""Bayesian Multi-Plate High-Throughput Screening of Compounds

	Can be used for joint identification of candidate compound hits from multiple assays, in drug discovery. This package implements the framework of I. D. Shterev, D. B. Dunson, C. Chan and G. D. Sempowski. "Bayesian Multi-Plate High-Throughput Screening of Compounds", Scientific Reports 8(1):9551, 2018. This project was funded by the Division of Allergy, Immunology, and Transplantation, National Institute of Allergy and Infectious Diseases, National Institutes of Health, Department of Health and Human Services, under contract No. HHSN272201400054C entitled "Adjuvant Discovery For Vaccines Against West Nile Virus and Influenza", awarded to Duke University and lead by Drs. Herman Staats and Soman Abraham.
	"""
	
	cran = "BHTSpack" 

	version("0.6", md5="9f22ba7123e8287357b4b7fafb74b3c8")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-r2html@2.3.2:", type=("build", "run"))
	depends_on("r-xtable@1.8.2:", type=("build", "run"))
