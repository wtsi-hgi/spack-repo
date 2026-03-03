# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBunchr(RPackage):
	"""Analyze Bunching in a Kink or Notch Setting

	View and analyze data where bunching is expected. Estimate counter-
    factual distributions. For earnings data, estimate the compensated
    elasticity of earnings w.r.t. the net-of-tax rate.
	"""
	
	homepage = "http://github.com/trilnick/bunchr"
	cran = "bunchr" 

	version("1.2.0", md5="07af4938efd036c57d0dbb0c40e6b14e")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-shiny@0.10.2:", type=("build", "run"))
