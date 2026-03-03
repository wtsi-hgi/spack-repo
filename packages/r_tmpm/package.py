# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmpm(RPackage):
	"""Trauma Mortality Prediction Model

	Trauma Mortality prediction for ICD-9, ICD-10, and AIS lexicons in
    long or wide format based on Dr. Alan Cook's tmpm mortality model.
	"""
	
	cran = "tmpm" 

	version("1.0.3", md5="a2a88fca131a27bdf7f740b344614760")

	depends_on("r-reshape2", type=("build", "run"))
