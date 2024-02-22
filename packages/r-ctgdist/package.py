# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtgdist(RPackage):
	"""Likert Category Distance Calculator

	It is assumed that psychological distances between the categories are equal for the measurement instruments consisted of polytomously scored items. According to Muraki, this assumption must be tested. In the examination process of this assumption, the fit indexes are obtained and evaluated. This package provides that this assumption is removed. By with this package, the converted scale values of all items in a measurement instrument can be calculated by estimating a category parameter set for each item. Thus, the calculations can be made without any need to usage of the common category parameter set. Through this package, the psychological distances of the items are scaled. The scaling of a category parameter set for each item cause differentiation of score of the categories will be got from items. Also, the total measurement instrument score of an individual can be calculated according to the scaling of item score categories by with this package.This package provides that the place of individuals related to the structure to be measured with a measurement instrument consisted of polytomously scored items can be reveal more accurately. In this way, it is thought that the results obtained about individuals can be made more sensitive, and the differences between individuals can be revealed more accurately. On the other hand, it can be argued that more accurate evidences can be obtained regarding the psychometric properties of the measurement instruments.
	"""
	
	cran = "ctgdist" 

	version("0.1.0", md5="bb692ac2458f48e202567645b2c75467")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
