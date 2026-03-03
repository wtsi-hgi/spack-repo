# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrape(RPackage):
	"""Gene-Ranking Analysis of Pathway Expression

	Gene-Ranking Analysis of Pathway Expression (GRAPE) is a tool for
   summarizing the consensus behavior of biological pathways in the form of a
   template, and for quantifying the extent to which individual samples deviate
   from the template. GRAPE templates are based only on the relative rankings
   of the genes within the pathway and can be used for classification of tissue
   types or disease subtypes. GRAPE can be used to represent gene-expression
   samples as vectors of pathway scores, where each pathway score indicates the
   departure from a given collection of reference samples. The resulting pathway-
   space representation can be used as the feature set for various applications,
   including survival analysis and drug-response prediction. 
   Users of GRAPE should use the following citation:
   Klein MI, Stern DF, and Zhao H. GRAPE: A pathway template method to characterize 
   tissue-specific functionality from gene expression profiles. 
   BMC Bioinformatics, 18:317 (June 2017).
	"""
	
	cran = "GRAPE" 

	version("0.1.1", md5="fe107571a3ff5ff2b44c245922f91920")

