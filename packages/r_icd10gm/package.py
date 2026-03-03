# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcd10gm(RPackage):
	"""Metadata Processing for the German Modification of the ICD-10
Coding System

	Provides convenient access to the German modification of the International Classification of Diagnoses, 10th revision (ICD-10-GM). It provides functionality to aid in the identification, specification and historisation of ICD-10 codes. Its intended use is the analysis of routinely collected data in the context of epidemiology, medical research and health services research. The underlying metadata are released by the German Institute for Medical Documentation and Information <https://www.dimdi.de>, and are redistributed in accordance with their license.
	"""
	
	homepage = "https://edonnachie.github.io/ICD10gm/"
	cran = "ICD10gm" 

	version("1.2.5", md5="6e9644f7f11bf4b6a14f945846edc87e")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
