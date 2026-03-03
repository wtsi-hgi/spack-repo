# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcr(RPackage):
	"""Analyzing Real-Time Quantitative PCR Data

	Calculates the amplification efficiency and curves from real-time 
  quantitative PCR (Polymerase Chain Reaction) data. Estimates the relative 
  expression from PCR data using the double delta CT and the standard curve 
  methods Livak & Schmittgen (2001) <doi:10.1006/meth.2001.1262>. Tests for 
  statistical significance using two-group tests and linear regression 
  Yuan et al. (2006) <doi: 10.1186/1471-2105-7-85>.
	"""
	
	homepage = "https://github.com/MahShaaban/pcr"
	cran = "pcr" 

	version("1.2.2", md5="604e49f072985465e41efcec9b7a01b1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
