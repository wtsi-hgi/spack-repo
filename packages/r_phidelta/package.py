# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhidelta(RPackage):
	"""Tool for Phi Delta Analysis of Features

	Analysis of features by phi delta diagrams. In particular, functions for reading data and calculating phi and delta as well as the functionality to plot it. Moreover it is possible to do further analysis on the data by generating rankings. For more information on phi delta diagrams, see also Giuliano Armano (2015) <doi:10.1016/j.ins.2015.07.028>.
	"""
	
	cran = "phiDelta" 

	version("1.0.1", md5="ff26c8035521f826234ee58dbc0602bb")

