# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbi(RPackage):
	"""Likelihood Based Inference

	Maximum likelihood estimation and likelihood ratio test are essential for modern statistics. This package supports in calculating likelihood based inference.
             Reference: Pawitan Y. (2001, ISBN:0-19-850765-8).
	"""
	
	homepage = "https://cran.r-project.org/package=LBI"
	cran = "LBI" 

	version("0.1.0", md5="38194c3a365048cd479193deb9ed1390")

	depends_on("r@3:", type=("build", "run"))
