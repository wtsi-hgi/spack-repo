# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHnp(RPackage):
	"""Half-Normal Plots with Simulation Envelopes

	Generates (half-)normal plots with simulation envelopes using different diagnostics from a range of different fitted models. A few example datasets are included.
	"""
	
	cran = "hnp" 

	version("1.2-6", md5="6b5353c65b1ce8028e22f819778498d3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass@7.3.35:", type=("build", "run"))
