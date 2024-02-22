# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFullroc(RPackage):
	"""Plot Full ROC Curves using Eyewitness Lineup Data

	Enable researchers to adjust identification rates using the 1/(lineup size) method, generate the full receiver operating characteristic (ROC) curves, and statistically compare the area under the curves (AUC). 
  References: Yueran Yang & Andrew Smith. (2020). "fullROC: An R package for generating and analyzing eyewitness-lineup ROC curves". <doi:10.13140/RG.2.2.20415.94885/1>  ,
              Andrew Smith, Yueran Yang, & Gary Wells. (2020). "Distinguishing between investigator discriminability and eyewitness discriminability: A method for creating full receiver operating characteristic curves of lineup identification performance". Perspectives on Psychological Science, 15(3), 589-607. <doi:10.1177/1745691620902426>.
	"""
	
	cran = "fullROC" 

	version("0.1.0", md5="45a6493b92f9daf1b8ef07aa4ec6b313")

