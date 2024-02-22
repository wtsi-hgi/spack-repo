# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcousticndlcoder(RPackage):
	"""Coding Sound Files for Use with NDL

	Make acoustic cues to use with the R packages 'ndl' or 'ndl2'. The package implements functions used
              in the PLoS ONE paper:
              Denis Arnold, Fabian Tomaschek, Konstantin Sering, Florence Lopez, and R. Harald Baayen (2017).
              Words from spontaneous conversational speech can be recognized with human-like accuracy by 
              an error-driven learning algorithm that discriminates between meanings straight from smart 
              acoustic features, bypassing the phoneme as recognition unit.  PLoS ONE 12(4):e0174623
              <doi:10.1371/journal.pone.0174623>
              More details can be found in the paper and the supplement.
              'ndl' is available on CRAN. 'ndl2' is available by request from <konstantin.sering@uni-tuebingen.de>.
	"""
	
	cran = "AcousticNDLCodeR" 

	version("1.0.2", md5="102705ab8ee33e0cc170c0ea42bba5b6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
