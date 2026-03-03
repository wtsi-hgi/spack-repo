# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedicalrisk(RPackage):
	"""Medical Risk and Comorbidity Tools for ICD-9-CM Data

	Generates risk estimates and comorbidity flags from ICD-9-CM
    codes available in administrative medical datasets. The package supports
    the Charlson Comorbidity Index, the Elixhauser Comorbidity
    classification, the Revised Cardiac Risk Index, and the Risk Stratification
    Index.  Methods are table-based, fast, and use the 'plyr' package, so
    parallelization is possible for large jobs. Also includes a sample of
    real ICD-9 data for 100 patients from a publicly available dataset.
	"""
	
	homepage = "https://github.com/patrickmdnet/medicalrisk"
	cran = "medicalrisk" 

	version("1.3", md5="6d790da7000d49fcacad856a39436d33")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr@1.5:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
