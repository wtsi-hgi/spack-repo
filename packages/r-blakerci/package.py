# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlakerci(RPackage):
	"""Blaker's Binomial and Poisson Confidence Limits

	Fast and accurate calculation of Blaker's binomial and Poisson confidence limits (and some related stuff).
	"""
	
	cran = "BlakerCI" 

	version("1.0-6", md5="311a954b771207d0c2de95c3ca484d63")

