# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInjuryseverityscore(RPackage):
	"""Translate ICD-9 into Injury Severity Score

	Calculate the injury severity score (ISS)
    based on the dictionary in 'ICDPIC' from <https://ideas.repec.org/c/boc/bocode/s457028.html>. The original code was written in 
    'STATA 11'. The original 'STATA' code was written by David Clark, 
    Turner Osler and David Hahn. I implement the same logic for easier access.
    Ref: David E. Clark & Turner M. Osler & David R. Hahn, 2009. 
    "ICDPIC: Stata module to provide methods for translating International 
    Classification of Diseases (Ninth Revision) diagnosis codes into standard injury 
    categories and/or scores," Statistical Software Components S457028, 
    Boston College Department of Economics, revised 29 Oct 2010.
	"""
	
	homepage = "https://github.com/dajuntian/InjurySeverityScore"
	cran = "InjurySeverityScore" 

	version("0.0.0.2", md5="7f8c1ec9a835199ec671c212ae2b606f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
