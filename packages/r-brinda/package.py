# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrinda(RPackage):
	"""Computation of BRINDA Adjusted Micronutrient Biomarkers for
Inflammation

	Inflammation can affect many micronutrient biomarkers and can thus lead to incorrect diagnosis of individuals and to over- or under-estimate the prevalence of deficiency in a population. Biomarkers Reflecting Inflammation and Nutritional Determinants of Anemia (BRINDA) is a multi-agency and multi-country partnership designed to improve the interpretation of nutrient biomarkers in settings of inflammation and to generate context-specific estimates of risk factors for anemia (Suchdev (2016) <doi:10.3945/an.115.010215>). In the past few years, BRINDA published a series of papers to provide guidance on how to adjust micronutrient biomarkers, retinol binding protein, serum retinol, serum ferritin by Namaste (2020), soluble transferrin receptor (sTfR), serum zinc, serum and Red Blood Cell (RBC) folate, and serum B-12, using inflammation markers, alpha-1-acid glycoprotein (AGP) and/or C-Reactive Protein (CRP) by Namaste (2020) <doi:10.1093/ajcn/nqaa141>, Rohner (2017) <doi:10.3945/ajcn.116.142232>, McDonald (2020) <doi:10.1093/ajcn/nqz304>, and Young (2020) <doi:10.1093/ajcn/nqz303>. The BRINDA inflammation adjustment method mainly focuses on Women of Reproductive Age (WRA) and Preschool-age Children (PSC); however, the general principle of the BRINDA method might apply to other population groups. The BRINDA R package is a user-friendly all-in-one R package that uses a series of functions to implement BRINDA adjustment method, as described above. The BRINDA R package will first carry out rigorous checks and provides users guidance to correct data or input errors (if they occur) prior to inflammation adjustments. After no errors are detected, the package implements the BRINDA inflammation adjustment for up to five micronutrient biomarkers, namely retinol-binding-protein, serum retinol, serum ferritin, sTfR, and serum zinc (when appropriate), using inflammation indicators of AGP and/or CRP for various population groups. Of note, adjustment for serum and RBC folate and serum B-12 is not included in the R package, since evidence shows that no adjustment is needed for these micronutrient biomarkers in either WRA or PSC groups (Young (2020) <doi:10.1093/ajcn/nqz303>).
	"""
	
	homepage = "https://github.com/hanqiluo/BRINDA"
	cran = "BRINDA" 

	version("0.1.5", md5="2efe2f21a59856d1d7cb70a1ae11a4c9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
