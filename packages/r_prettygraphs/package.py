# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettygraphs(RPackage):
	"""Publication-Quality Graphics

	Simple and crisp publication-quality graphics for the ExPosition family of packages.
  See An ExPosition of the Singular Value Decomposition in R (Beaton et al 2014) <doi:10.1016/j.csda.2013.11.006>.
	"""
	
	cran = "prettyGraphs" 

	version("2.1.6", md5="b11858ac7131c3fe23fe9760c3b711f0")

