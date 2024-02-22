# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoebinning(RPackage):
	"""Supervised Weight of Evidence Binning of Numeric Variables and
Factors

	Implements an automated binning of numeric variables and factors with
 respect to a dichotomous target variable.
 Two approaches are provided: An implementation of fine and coarse classing that
 merges granular classes and levels step by step. And a tree-like approach that
 iteratively segments the initial bins via binary splits. Both procedures merge,
 respectively split, bins based on similar weight of evidence (WOE) values and
 stop via an information value (IV) based criteria.
 The package can be used with single variables or an entire data frame. It provides
 flexible tools for exploring different binning solutions and for deploying them to
 (new) data.
	"""
	
	cran = "woeBinning" 

	version("0.1.6", md5="47a521518385cdda07fd3ff42d519c49")

