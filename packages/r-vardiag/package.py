# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVardiag(RPackage):
	"""Variogram Diagnostics

	Interactive variogram diagnostics.
	"""
	
	homepage = "https://github.com/edzer/vardiag/"
	cran = "vardiag" 

	version("0.2-1", md5="1a1d380bc670bd63f623293d24638e3d")

	depends_on("r@2:", type=("build", "run"))
