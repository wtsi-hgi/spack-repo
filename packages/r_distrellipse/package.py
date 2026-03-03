# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrellipse(RPackage):
	"""S4 Classes for Elliptically Contoured Distributions

	Distribution (S4-)classes for elliptically contoured distributions (based on
            package 'distr').
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrEllipse" 

	version("2.8.2", md5="561743d64c6d5929f4d511f047a49c76")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-setrng@2006.2.1:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-distrsim@2.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
