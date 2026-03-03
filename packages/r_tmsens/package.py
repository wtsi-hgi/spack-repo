# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmsens(RPackage):
	"""Sensitivity Analysis Using the Trimmed Means Estimator

	Sensitivity analysis using the trimmed means estimator.
	"""
	
	homepage = "https://github.com/dea-hazewinkel/tmsens"
	cran = "tmsens" 

	version("0.3.0", md5="213b89121e1fe7c9edd246636bf50c70")

