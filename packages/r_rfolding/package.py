# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfolding(RPackage):
	"""The Folding Test of Unimodality

	The basic algorithm to perform the folding test of unimodality. 
  Given a dataset X (d dimensional, n samples), the test checks whether the 
  distribution of the data are rather unimodal or rather multimodal. This 
  package stems from the following research publication: 
  Siffer Alban, Pierre-Alain Fouque, Alexandre Termier, and Christine Largouët. 
  "Are your data gathered?" In Proceedings of the 24th ACM SIGKDD International 
  Conference on Knowledge Discovery Data Mining, pp. 2210-2218. ACM, 2018.
  <doi:10.1145/3219819.3219994>.
	"""
	
	cran = "Rfolding" 

	version("1.0", md5="343caa61c8a3abc7524b6b5743d33b5f")

