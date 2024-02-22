# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKtensorgraphs(RPackage):
	"""Co-Tucker3 Analysis of Two Sequences of Matrices

	Provides a function called COTUCKER3() (Co-Inertia Analysis
    + Tucker3 method) which performs a Co-Tucker3 analysis of two sequences of
    matrices, as well as other functions called PCA() (Principal Component Analysis)
    and BGA() (Between-Groups Analysis), which perform analysis of one matrix,
    COIA() (Co-Inertia Analysis), which performs analysis of two matrices, PTA()
    (Partial Triadic Analysis), STATIS(), STATISDUAL() and TUCKER3(), which perform analysis of a sequence
    of matrices, and BGCOIA() (Between-Groups Co-Inertia Analysis), STATICO()
    (STATIS method + Co-Inertia Analysis), COSTATIS() (Co-Inertia Analysis + STATIS
    method), which also perform analysis of two sequences of matrices.
	"""
	
	cran = "KTensorGraphs" 

	version("1.1", md5="c60716827ed30f7b32a6106e7a400212")

