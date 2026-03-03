# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVudc(RPackage):
	"""Visualization of Univariate Data for Comparison

	Contains functions for visualization univariate data: ccdplot and qddplot.
	"""
	
	cran = "vudc" 

	version("1.1", md5="d08bd2da881fe7c25139d534a951c663")

