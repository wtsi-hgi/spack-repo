# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKertests(RPackage):
	"""Generalized Kernel Two-Sample Tests

	New kernel-based test and fast tests for testing whether two samples are from the same distribution. They work well particularly for high-dimensional data.
      Song, H. and Chen, H. (2023) 
      <arXiv:2011.06127>.
	"""
	
	cran = "kerTests" 

	version("0.1.4", md5="9ad04e3f634919bc8a52b11e85c70de4")

