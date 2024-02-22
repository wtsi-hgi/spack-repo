# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdlm(RPackage):
	"""Systematic Comparison of Trip Distribution Laws and Models

	The main purpose of this package is to propose a rigorous framework to fairly compare trip distribution laws and models as described in Lenormand et al. (2016) <doi:10.1016/j.jtrangeo.2015.12.008>.
	"""
	
	homepage = "https://epivec.github.io/TDLM/"
	cran = "TDLM" 

	version("1.0.0", md5="f83260273d6544de056d1b88d2376777")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ecume", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rdpack@1:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-rmarkdown@2:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
