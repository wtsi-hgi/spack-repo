# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSac(RPackage):
	"""Semiparametric Analysis of Change-Point

	Semiparametric empirical likelihood ratio
    based tests of change-point with one-change or epidemic alternatives
    with data-based model diagnostic are contained.
	"""
	
	cran = "sac" 

	version("1.0.2", md5="b37c5d274eb72540ce9b58d54a2e9349")

	depends_on("r@1.4:", type=("build", "run"))
