# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecode(RPackage):
	"""Differential Co-Expression and Differential Expression Analysis

	Integrated differential expression (DE) and differential co-expression (DC) analysis on gene expression data based on DECODE (DifferEntial CO-expression and Differential Expression) algorithm.
	"""
	
	cran = "decode" 

	version("1.2", md5="1a1270b455443c5ebaddb3ec3f66f432")

	depends_on("r@3.1.2:", type=("build", "run"))
