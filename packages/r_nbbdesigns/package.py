# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbbdesigns(RPackage):
	"""Neighbour Balanced Block Designs (NBBDesigns)

	Neighbour-balanced designs ensure that no treatment is disadvantaged unfairly by its surroundings. The treatment allocation in these designs is such that every treatment appears equally often as a neighbour with every other treatment. Neighbour Balanced Designs are employed when there is a possibility of neighbour effects from treatments used in adjacent experimental units. In the literature, a vast number of such designs have been developed. This package generates some efficient neighbour balanced block designs which are balanced and partially variance balanced for estimating the contrast pertaining to direct and neighbour effects, as well as provides a function for analysing the data obtained from such trials (Azais, J.M., Bailey, R.A. and Monod, H. (1993). "A catalogue of efficient neighbour designs with border plots". Biometrics, 49, 1252-1261 ; Tomar, J. S., Jaggi, Seema and Varghese, Cini (2005)<DOI: 10.1080/0266476042000305177>. "On totally balanced block designs for competition effects"). This package contains functions named nbbd1(),nbbd2(),nbbd3(),pnbbd1() and pnbbd2() which generates neighbour balanced block designs within a specified range of number of treatment (v). It contains another function named anlys()for performing the analysis of data generated from such trials.
	"""
	
	cran = "NBBDesigns" 

	version("1.1.0", md5="4b9448b5e0674c367c2837aeda5d6b1a")

	depends_on("r@3.5:", type=("build", "run"))
