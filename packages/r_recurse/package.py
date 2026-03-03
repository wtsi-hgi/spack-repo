# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecurse(RPackage):
	"""Computes Revisitation Metrics for Trajectory Data

	Computes revisitation metrics for trajectory data, such as the number of revisitations for each location as well as the time spent for that visit and the time since the previous visit. Also includes functions to plot data.
	"""
	
	cran = "recurse" 

	version("1.3.0", md5="02e0343feb581268d9df5e13c0203826")

	depends_on("r-rcpp", type=("build", "run"))
