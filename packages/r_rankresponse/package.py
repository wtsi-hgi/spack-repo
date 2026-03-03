# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankresponse(RPackage):
	"""Ranking Responses in a Single Response Question or a Multiple
Response Question

	Methods for ranking responses of a single response question or a 
  multiple response question are described in the two papers: 
  1. Wang, H. (2008). Ranking Responses in Multiple-Choice Questions. Journal of 
  Applied Statistics, 35, 465-474. <DOI:10.1080/02664760801924533> 
  2. Wang, H. and Huang, W. H. (2014). Bayesian Ranking Responses in Multiple 
  Response Questions. Journal of the Royal Statistical Society: Series A 
  (Statistics in Society), 177, 191-208. <DOI:10.1111/rssa.12009>. 
	"""
	
	cran = "RankResponse" 

	version("4.0.0", md5="59345b68f69a64de5dfd100199d32600")

