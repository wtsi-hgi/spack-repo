# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKpcalg(RPackage):
	"""Kernel PC Algorithm for Causal Structure Detection

	Kernel PC (kPC) algorithm for causal structure learning and causal inference using graphical models. kPC is a version of PC algorithm that uses kernel based independence criteria in order to be able to deal with non-linear relationships and non-Gaussian noise.
	"""
	
	cran = "kpcalg" 

	version("1.0.1", md5="4434ac992201d98f7a15add6fe3551f5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
