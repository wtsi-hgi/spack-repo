# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgus(RPackage):
	"""Random Variate Generator for the Argus Distribution

	
  Random variate generation, density, CDF and quantile function 
  for the Argus distribution. Especially, it includes for random variate generation a
  flexible inversion method that is also fast in the varying parameter case.
  A Ratio-of-Uniforms method is provided as second alternative.
	"""
	
	cran = "argus" 

	version("0.1.1", md5="c55c1aaf269a39cffd6449f62bfe7aa8")

	depends_on("r-runuran", type=("build", "run"))
