# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultbxxc(RPackage):
	"""Auxiliary Routines for Influx Software

	Contains auxiliary routines for influx software. This packages is not intended to be used directly. Influx was published here: Sokol et al. (2012) <doi:10.1093/bioinformatics/btr716>.
	"""
	
	homepage = "https://metasys.insa-toulouse.fr/software/influx/"
	cran = "multbxxc" 

	version("1.0.1", md5="22f9e23bec6e5ddfd89691aeae3fb601")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rmumps", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
