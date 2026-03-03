# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrrcac(RPackage):
	"""Computing Chance-Corrected Agreement Coefficients (CAC)

	Calculates various chance-corrected agreement coefficients (CAC) among 2 or more raters are provided. 
	Among the CAC coefficients covered are Cohen's kappa, Conger's kappa, Fleiss' kappa, Brennan-Prediger coefficient, Gwet's AC1/AC2 
	coefficients, and Krippendorff's alpha. Multiple sets of weights are proposed for computing weighted analyses. All of these statistical 
	procedures are described in details in Gwet, K.L. (2014,ISBN:978-0970806284): "Handbook of Inter-Rater Reliability," 4th edition, 
	Advanced Analytics, LLC.
	"""
	
	cran = "irrCAC" 

	version("1.0", md5="163289021aa54557c3433e5f57401b4f")

