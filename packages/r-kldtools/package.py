# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKldtools(RPackage):
	"""Kullback-Leibler Divergence and Other Tools to Analyze
Frequencies

	Most importantly, calculates Kullback-Leibler Divergence (KLD), Turing's perspective estimator
 and their confidence intervals.
	"""
	
	cran = "kldtools" 

	version("1.2", md5="54f3eb67d8e5620b16062256cc65ffd7")

