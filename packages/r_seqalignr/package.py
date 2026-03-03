# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqalignr(RPackage):
	"""Sequence Alignment and Visualization Tool

	Computes the optimal alignment of two character sequences.
    Visualizes the result of the alignment in a matrix plot.
    Needleman, Saul B.; Wunsch, Christian D. (1970) "A general method applicable to the search for similarities in the amino acid sequence of two proteins" <doi:10.1016/0022-2836(70)90057-4>.
	"""
	
	cran = "SeqAlignR" 

	version("0.1.1", md5="aa5a026f99c6a8d074954c3246732a7a")

	depends_on("r-plot-matrix", type=("build", "run"))
