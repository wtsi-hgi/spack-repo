# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrrmetrics(RPackage):
	"""Distribution Classes for Distributions from Rmetrics

	S4-distribution classes based on package distr for distributions from packages
            'fBasics' and 'fGarch'.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrRmetrics" 

	version("2.8.2", md5="9af3282aacb56eb7704e0e9caa8c60a3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.4:", type=("build", "run"))
	depends_on("r-fbasics@270.73:", type=("build", "run"))
	depends_on("r-fgarch@270.73:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
