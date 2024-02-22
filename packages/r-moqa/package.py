# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoqa(RPackage):
	"""Basic Quality Data Assurance for Epidemiological Research

	With the provision of several tools and templates the MOSAIC project (DFG-Grant Number HO 1937/2-1) supports the implementation of a central data management in epidemiological research projects. The 'MOQA' package enables epidemiologists with none or low experience in R to generate basic data quality reports for a wide range of application scenarios. See <https://mosaic-greifswald.de/> for more information. Please read and cite the corresponding open access publication (using the former package-name) in METHODS OF INFORMATION IN MEDICINE by M. Bialke, H. Rau, T. Schwaneberg, R. Walk, T. Bahls and W. Hoffmann (2017) <doi:10.3414/ME16-01-0123>. <https://methods.schattauer.de/en/contents/most-recent-articles/issue/2483/issue/special/manuscript/27573/show.html>.
	"""
	
	cran = "MOQA" 

	version("2.0.0", md5="0cccbb82c1625db24721fe7624f9c657")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
