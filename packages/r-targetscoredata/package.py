# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetscoredata(RPackage):
	"""TargetScoreData

	Precompiled and processed miRNA-overexpression fold-changes from 84 Gene Expression Omnibus (GEO) series corresponding to 6 platforms, 77 human cells or tissues, and 113 distinct miRNAs. Accompanied with the data, we also included in this package the sequence feature scores from TargetScanHuman 6.1 including the context+ score and the probabilities of conserved targeting for each miRNA-mRNA interaction. Thus, the user can use these static sequence-based scores together with user-supplied tissue/cell-specific fold-change due to miRNA overexpression to predict miRNA targets using the package TargetScore (download separately)
	"""
	
	bioc = "TargetScoreData"

	version("1.44.0", commit="c2f138c407daa667e29bc4509b63791d48635e74")
	version("1.38.0", commit="4d2f19ed17aeaa51782eaa409dafc97a661bb15d")


