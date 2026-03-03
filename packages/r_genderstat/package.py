# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenderstat(RPackage):
	"""Quantitative Analysis Tools for Gender Studies

	Provides tools for quantitative analysis in gender studies, including functions to calculate various gender inequality metrics such as the Gender Pay Gap, Gender Inequality Index (GII), Gender Development Index (GDI), and Gender Empowerment Measure (GEM). Also includes extracted real datasets for practice and learning purposes, which were obtained from the UNDP Human Development Reports Data Center <https://hdr.undp.org/data-center/documentation-and-downloads> and the World Bank Gender Data Portal <https://genderdata.worldbank.org/indicators/>. References: Miller, Kevin; Vagins, Deborah J. (2021) <https://eric.ed.gov/?id=ED596219>. Jacques Charmes & Saskia Wieringa (2003) <doi:10.1080/1464988032000125773>. Gaëlle Ferrant (2010) <https://shs.hal.science/halshs-00462463/>.
	"""
	
	cran = "genderstat" 

	version("0.1.3", md5="44f5ad1ec7fbd2e93dd263afb970fb6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
