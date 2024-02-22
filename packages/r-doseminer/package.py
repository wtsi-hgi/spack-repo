# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoseminer(RPackage):
	"""Extract Drug Dosages from Free-Text Prescriptions

	Utilities for converting unstructured electronic prescribing instructions into structured medication data. Extracts drug dose, units, daily dosing frequency and intervals from English-language prescriptions. Based on Karystianis et al. (2015) <doi:10.1186/s12911-016-0255-x>.
	"""
	
	cran = "doseminer" 

	version("0.1.2", md5="25ef9bb8e9e42d1a90ef8d822f5265f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
