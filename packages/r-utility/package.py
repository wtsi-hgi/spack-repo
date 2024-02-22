# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtility(RPackage):
	"""Construct, Evaluate and Plot Value and Utility Functions

	Construct and plot objective hierarchies and associated value and utility functions. 
  Evaluate the values and utilities and visualize the results as colored objective hierarchies or tables. 
  Visualize uncertainty by plotting median and quantile intervals within the nodes of objective hierarchies.
  Get numerical results of the evaluations in standard R data types for further processing.
	"""
	
	cran = "utility" 

	version("1.4.6", md5="ea5aabb0950f492cfc4df459b12846b5")

