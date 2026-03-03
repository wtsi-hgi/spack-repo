# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQboxplot(RPackage):
	"""Quantile-Based Boxplot

	Produce quantile-based box-and-whisker plot(s).
	"""
	
	cran = "qboxplot" 

	version("0.2", md5="72387bc7d04dd420d9c342b466ef1a39")

