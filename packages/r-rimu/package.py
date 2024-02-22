# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimu(RPackage):
	"""Responses in Multiplex

	Tools for manipulating, exploring, and visualising  multiple-response data, including scored or ranked responses. Conversions to and from factors, lists, strings, matrices; reordering, lumping, flattening; set operations; tables; frequency and co-occurrence plots.
	"""
	
	cran = "rimu" 

	version("0.6", md5="19996a838188b5e56dcd812260daac94")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
