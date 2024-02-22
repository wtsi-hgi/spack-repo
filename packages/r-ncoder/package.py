# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcoder(RPackage):
	"""Techniques for Automated Classifiers

	A set of techniques that can be used to develop, validate, and implement automated classifiers. A powerful tool for transforming raw data into meaningful information, 'ncodeR' (Shaffer, D. W. (2017) Quantitative Ethnography. ISBN: 0578191687) is designed specifically for working with big data: large document collections, logfiles, and other text data.
	"""
	
	cran = "ncodeR" 

	version("0.2.0.1", md5="2a2e653cd825c71813aaac3db78c7986")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rhor", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
