# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodycomp(RPackage):
	"""Percent Body Fat Values Using Anthropometric Prediction
Equations

	Skinfold measurements is one of the most popular and practical methods for estimating percent body fat. Body composition is a term that describes the relative proportions of fat, bone, and muscle mass in the human body. Following the collection of skinfold measurements, regression analysis (a statistical procedure used to predict a dependent variable based on one or more independent or predictor variables) is used to estimate total percent body fat in humans. <doi:10.4324/9780203868744>. 
	"""
	
	cran = "bodycomp" 

	version("1.0.0", md5="fb22503aa1fada789ebf4845bbd669b5")

