# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethped(RPackage):
	"""A DNA methylation classifier tool for the identification of pediatric brain tumor subtypes

	Classification of pediatric tumors into biologically defined subtypes is challenging and multifaceted approaches are needed. For this aim, we developed a diagnostic classifier based on DNA methylation profiles. We offer MethPed as an easy-to-use toolbox that allows researchers and clinical diagnosticians to test single samples as well as large cohorts for subclass prediction of pediatric brain tumors.  The current version of MethPed can classify the following tumor diagnoses/subgroups: Diffuse Intrinsic Pontine Glioma (DIPG), Ependymoma, Embryonal tumors with multilayered rosettes (ETMR), Glioblastoma (GBM), Medulloblastoma (MB) - Group 3 (MB_Gr3), Group 4 (MB_Gr3), Group WNT (MB_WNT), Group SHH (MB_SHH) and Pilocytic Astrocytoma (PiloAstro).
	"""
	
	bioc = "MethPed"

	version("1.36.0", commit="6c9b6885d7ad8c178f72fbb1a8d8ff37d9ad8d00")
	version("1.30.0", commit="1b88a6f0477f822d99130b9feec758b221cdf72c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
