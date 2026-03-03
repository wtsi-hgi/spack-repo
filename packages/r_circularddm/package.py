# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircularddm(RPackage):
	"""Circular Drift-Diffusion Model

	Circular drift-diffusion model for continuous reports.
	"""
	
	cran = "CircularDDM" 

	version("0.1.0", md5="3dfef6ea2a3634c980c117658a54b0f3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.6.700.6:", type=("build", "run"))
