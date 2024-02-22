# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElliplot(RPackage):
	"""Ellipse Summary Plot of Quantiles

	Correlation chart of two set (x and y) of data.  
  Using Quantiles.  Visualize the effect of factor. 
	"""
	
	cran = "elliplot" 

	version("1.3.0", md5="c5175a1e55906930d58068df4f58290e")

