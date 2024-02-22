# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptmt(RPackage):
	"""Adaptive P-Value Thresholding for Multiple Hypothesis Testing
with Side Information

	Implementation of adaptive p-value thresholding (AdaPT), including both a framework that allows the user to specify any 
  algorithm to learn local false discovery rate and a pool of convenient functions that implement specific 
  algorithms. See Lei, Lihua and Fithian, William (2016) <arXiv:1609.06035>.
	"""
	
	homepage = "https://arxiv.org/abs/1609.06035"
	cran = "adaptMT" 

	version("1.0.0", md5="6871be7bdaf46a4e537b2d0927b6b40a")

