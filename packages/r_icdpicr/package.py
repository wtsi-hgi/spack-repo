# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcdpicr(RPackage):
	"""'ICD' Programs for Injury Categorization in R

	Categorization and scoring of injury severity typically involves
    trained personnel with access to injured persons or their medical records. 'icdpicr' contains a function
    that provides automated calculation of Abbreviated Injury Scale ('AIS') and Injury Severity Score ('ISS')
    from International Classification of Diseases ('ICD') codes and may be a useful substitute to manual injury 
    severity scoring. 'ICDPIC' was originally developed in 'Stata', and 'icdpicr' is an open-access update 
    that accepts both 'ICD-9' and 'ICD-10' codes. 
	"""
	
	cran = "icdpicr" 

	version("1.0.1", md5="be57fc4e558f84bcfa34464873167e60")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
