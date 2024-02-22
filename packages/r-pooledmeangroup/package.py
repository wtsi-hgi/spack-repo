# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooledmeangroup(RPackage):
	"""Pooled Mean Group Estimation of Dynamic Heterogenous Panels

	Calculates the pooled mean group (PMG) estimator for dynamic panel data models, as described by Pesaran, Shin and Smith (1999) <doi:10.1080/01621459.1999.10474156>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "PooledMeanGroup" 

	version("1.0", md5="181b2f249b144f946a20b1e4aa0ca89d")

	depends_on("r@3.2.3:", type=("build", "run"))
