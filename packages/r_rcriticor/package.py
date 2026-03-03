# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcriticor(RPackage):
	"""Pierre-Goldwin Correlogram

	Goldwin-Pierre correlogram. Research of critical periods in the past. Integrates a time series in a given window.  
	"""
	
	cran = "Rcriticor" 

	version("2.0", md5="8e323bf2b685fe7f39a4cfaeee1f6a22")

	depends_on("r@3.2:", type=("build", "run"))
