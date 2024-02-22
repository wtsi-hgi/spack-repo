# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR1magic(RPackage):
	"""Compressive Sampling: Sparse Signal Recovery Utilities

	Utilities for sparse signal recovery suitable for compressed sensing. L1, L2 and TV penalties, DFT basis matrix, simple sparse signal generator, mutual cumulative coherence between two matrices and examples, Lp complex norm, scaling back regression coefficients.
	"""
	
	cran = "R1magic" 

	version("0.3.4", md5="6a066bbb4b542c07913929ef796a7a1c")

