# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikelihood(RPackage):
	"""Methods for Maximum Likelihood Estimation

	Tools for maximum likelihood estimation of parameters 
  of scientific models. Based on Goffe et al (1994) <doi:10.1016/0304-4076(94)90038-8>.
	"""
	
	cran = "likelihood" 

	version("1.9", md5="c5d93817e1518a5ec186ee35a9a23c9a")

	depends_on("r@2.1.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
