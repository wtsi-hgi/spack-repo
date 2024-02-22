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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MethPed_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MethPed/MethPed_1.30.0.tar.gz"]

	version("1.30.0", md5="57b633da5d8548342b0a2071efe3c04d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
