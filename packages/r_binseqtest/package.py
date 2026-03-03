# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinseqtest(RPackage):
	"""Exact Binary Sequential Designs and Analysis

	For a series of binary responses, create stopping boundary with exact results after stopping, allowing updating for missing assessments.
	"""
	
	cran = "binseqtest" 

	version("1.0.4", md5="fc45afd8370f16e38b043301ea99c4d5")

	depends_on("r-clinfun", type=("build", "run"))
