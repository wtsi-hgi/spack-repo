# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGte(RPackage):
	"""Generalized Turnbull's Estimator

	Generalized Turnbull's estimator proposed by Dehghan and Duchesne
    (2011).
	"""
	
	cran = "gte" 

	version("1.2-3", md5="f37166aaf2825ded7e64677c83cf24a6")

	depends_on("r-survival", type=("build", "run"))
