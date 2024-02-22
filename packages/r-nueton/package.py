# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNueton(RPackage):
	"""Nitrogen Use Efficiency Toolkit on Numerics

	Comprehensive R package designed to facilitate the calculation of Nitrogen Use Efficiency (NUE) indicators using experimentally derived data. The package incorporates 23 parameters categorized into six fertilizer-based, four plant-based, three soil-based, three isotope-based, two ecology-based, and four system-based indicators, providing a versatile platform for NUE assessment. As of the current version, 'NUETON' serves as a starting point for users to compute NUE indicators from their experimental data. Future updates are planned to enhance the package's capabilities, including robust data visualization tools and error margin consideration in calculations. Additionally, statistical methods will be integrated to ensure the accuracy and reliability of the calculated indicators. All formulae used in 'NUETON' are thoroughly referenced within the source code, and the package is released as open source software. Users are encouraged to provide feedback and contribute to the improvement of this package. It is important to note that the current version of 'NUETON' is not intended for rigorous research purposes, and users are responsible for validating their results. The package developers do not assume liability for any inaccuracies in calculations. This package includes content from Congreves KA, Otchere O, Ferland D, Farzadfar S, Williams S and Arcand MM (2021) 'Nitrogen Use Efficiency Definitions of Today and Tomorrow.' Front. Plant Sci. 12:637108. <doi:10.3389/fpls.2021.637108>. The article is available under the Creative Commons Attribution License (CC BY) C. 2021 Congreves, Otchere, Ferland, Farzadfar, Williams and Arcand.
	"""
	
	cran = "NUETON" 

	version("0.1.0", md5="96da344b5cd5ff0f2566aa489d5d4679")

