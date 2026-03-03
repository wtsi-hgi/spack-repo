# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRinsp(RPackage):
	"""R Individual Specialization

	Functions to calculate several ecological indices of individual 
    and population niche width (Araujo's E, clustering and pairwise similarity 
    among individuals, IS, Petraitis' W, and Roughgarden's WIC/TNW) to assess 
    individual specialization based on data of resource use. Resource use can 
    be quantified by counts of categories, measures of mass or length, or 
    proportions. Monte Carlo resampling procedures are available for hypothesis 
    testing against multinomial null models.
    Details are provided in Zaccarelli et al. (2013) <doi:10.1111/2041-210X.12079>
    and associated references.
	"""
	
	cran = "RInSp" 

	version("1.2.5", md5="266ce75504d8e273db69de47665a6268")

