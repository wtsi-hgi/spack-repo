# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZfit(RPackage):
	"""Fit Models in a Pipe

	Improve the usage of model fitting functions within a piped
    work flow.
	"""
	
	homepage = "https://torfason.github.io/zfit/"
	cran = "zfit" 

	version("0.4.0", md5="16e5b89ce2343e4f9e984e0bc4ee302a")

	depends_on("r@3.5:", type=("build", "run"))
