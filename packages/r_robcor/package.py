# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobcor(RPackage):
	"""Robust Correlations

	Robust pairwise correlations based on estimates of scale,
  particularly on "FastQn" one-step M-estimate.
	"""
	
	cran = "robcor" 

	version("0.1-6.1", md5="4225109b2c085305029d19b31b99773c")

	depends_on("r@2.10:", type=("build", "run"))
