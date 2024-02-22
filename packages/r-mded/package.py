# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMded(RPackage):
	"""Measuring the Difference Between Two Empirical Distributions

	Provides a function for measuring the difference between two independent or non-independent empirical distributions and returning a significance level of the difference.
	"""
	
	cran = "mded" 

	version("0.1-2", md5="0e752e8df0a44efdcd71368f0a05e8fa")

