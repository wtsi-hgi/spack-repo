# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcdData(RPackage):
	"""International Classifcation of Diseases (ICD) Data

	Data from the United States Center for Medicare and Medicaid
    Services (CMS) is included in this package. There are ICD-9 and ICD-10
    diagnostic and procedure codes, and lists of the chapter and sub-chapter 
    headings and the ranges of ICD codes they encompass. There are also two 
    sample datasets. These data are used by the 'icd' package for finding
    comorbidities.
	"""
	
	cran = "icd.data" 

	version("1.0", md5="57e5350fe3c430b6270f74c5d83c31c7")

	depends_on("r@3:", type=("build", "run"))
