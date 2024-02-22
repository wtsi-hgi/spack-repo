# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsplines(RPackage):
	"""Quaternions Splines

	Provides routines to create some quaternions splines:
    Barry-Goldman algorithm, De Casteljau algorithm, and Kochanek-Bartels
    algorithm. The implementations are based on the Python library
    'splines'. Quaternions splines allow to construct spherical curves. 
    References: Barry and Goldman <doi:10.1145/54852.378511>, 
    Kochanek and Bartels <doi:10.1145/800031.808575>.
	"""
	
	homepage = "https://github.com/stla/qsplines"
	cran = "qsplines" 

	version("1.0.1", md5="73814c0d760a1243ffb4d95368d61c0d")

	depends_on("r-onion", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
