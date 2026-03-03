# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrricc(RPackage):
	"""Intraclass Correlations for Quantifying Inter-Rater Reliability

	Calculates various intraclass correlation coefficients used to quantify 
  inter-rater and intra-rater reliability.  The assumption here is that the raters produced quantitative ratings. Most of the statistical procedures implemented
  in this package are described in details in Gwet, K.L. (2014, ISBN:978-0970806284): "Handbook of Inter-Rater Reliability," 4th edition, 
  Advanced Analytics, LLC.
	"""
	
	cran = "irrICC" 

	version("1.0", md5="74b7f6370f75362d5cf9d72b53adf4f7")

