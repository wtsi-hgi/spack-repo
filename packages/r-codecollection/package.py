# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodecollection(RPackage):
	"""Collection of Codes with Labels

	Includes several classifications such as International Statistical Classification of  Diseases and Related Health Problems 10th Revision (ICD10),  Anatomical Therapeutic Chemical (ATC) Classification,  The International Classification of Diseases for Oncology (ICD-O-3), and  International Classification of Primary Care (ICPC). Includes function that adds descriptive label to code value.  Depending on classification following languages are available: English, Finnish, Swedish, and Latin.
	"""
	
	cran = "codeCollection" 

	version("0.1.3", md5="039c258fbcc919bf07188df9d1d8ef64")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
