# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondvis(RPackage):
	"""Conditional Visualization for Statistical Models

	Exploring fitted models by interactively taking 2-D and 3-D
  sections in data space.
	"""
	
	homepage = "http://markajoc.github.io/condvis/"
	cran = "condvis" 

	version("0.5-1", md5="1a57b5c704a5e77c8a5e9866b7cd051d")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
