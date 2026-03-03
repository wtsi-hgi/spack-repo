# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpr(RPackage):
	"""Temporal Process Regression

	Regression models for temporal process responses with
        time-varying coefficient.
	"""
	
	cran = "tpr" 

	version("0.3-3", md5="83c72ef6b867a1a2d2cc607409889d6e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lgtdl", type=("build", "run"))
