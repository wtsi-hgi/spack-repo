# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvna(RPackage):
	"""Nelson-Aalen Estimator of the Cumulative Hazard in Multistate
Models

	Computes the Nelson-Aalen estimator of the cumulative transition hazard for arbitrary Markov multistate models <ISBN:978-0-387-68560-1>. 
	"""
	
	cran = "mvna" 

	version("2.0.1", md5="190a66ac1e4da1f5887525fba5d0b5dc")

	depends_on("r-lattice", type=("build", "run"))
