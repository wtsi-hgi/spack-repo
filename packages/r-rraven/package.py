# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRraven(RPackage):
	"""Connecting R and 'Raven' Sound Analysis Software

	A tool to exchange data between R and 'Raven' sound analysis software (Cornell Lab of Ornithology). Functions work on data formats compatible with the R package 'warbleR'.
	"""
	
	homepage = "https://github.com/maRce10/Rraven"
	cran = "Rraven" 

	version("1.0.13", md5="fda87bf39250734c2813d83081e489cf")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-warbler", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-naturesounds", type=("build", "run"))
