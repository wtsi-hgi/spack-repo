# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongmemo(RPackage):
	"""Statistics for Long-Memory Processes (Book Jan Beran), and
Related Functionality

	Datasets and Functionality from
  'Jan Beran' (1994). Statistics for Long-Memory Processes; Chapman & Hall.
  Estimation of Hurst (and more) parameters for fractional Gaussian noise,
  'fARIMA' and 'FEXP' models.
	"""
	
	cran = "longmemo" 

	version("1.1-2", md5="38024ac19d25d74308cef550d2960bd4")

