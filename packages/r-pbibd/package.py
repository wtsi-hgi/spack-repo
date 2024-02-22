# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbibd(RPackage):
	"""Partially Balanced Incomplete Block Designs

	The PBIB designs are important type of incomplete block designs having wide area of their applications for example in agricultural experiments, in plant breeding, in sample surveys etc. This package constructs various series of PBIB designs and assists in checking all the necessary conditions of PBIB designs and the association scheme on which these designs are based on. It also assists in calculating the efficiencies of PBIB designs with any number of associate classes. The package also constructs Youden-m square designs which are Row-Column designs for the two-way elimination of heterogeneity. The incomplete columns of these Youden-m square designs constitute PBIB designs. With the present functionality, the package will be of immense importance for the researchers as it will help them to construct PBIB designs, to check if their PBIB designs and association scheme satisfy various necessary conditions for the existence, to calculate the efficiencies of PBIB designs based on any association scheme and to construct Youden-m square designs for the two-way elimination of heterogeneity. R. C. Bose and K. R. Nair (1939) <http://www.jstor.org/stable/40383923>.
	"""
	
	cran = "PBIBD" 

	version("1.3", md5="0ccf08310cca5d5143e7f536a9de184e")

