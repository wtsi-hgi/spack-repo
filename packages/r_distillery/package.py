# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistillery(RPackage):
	"""Method Functions for Confidence Intervals and to Distill
Information from an Object

	Some very simple method functions for confidence interval calculation, bootstrap resampling aimed at atmospheric science applications, and to distill pertinent information from a potentially complex object; primarily used in common with packages extRemes and SpatialVx.  To reference this package and for a tutorial on the bootstrap functions, please see Gilleland (2020) <doi: 10.1175/JTECH-D-20-0069.1> and Gilleland (2020) <doi: 10.1175/JTECH-D-20-0070.1>.
	"""
	
	homepage = "https://ral.ucar.edu/staff/ericg/"
	cran = "distillery" 

	version("1.2-1", md5="239696bd8b41ce225a7b0a80656d5e21")

	depends_on("r@2.10:", type=("build", "run"))
