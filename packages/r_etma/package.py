# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtma(RPackage):
	"""Epistasis Test in Meta-Analysis

	Traditional meta-regression based method has been developed for using meta-analysis data, but it faced the challenge of inconsistent estimates. This package purpose a new statistical method to detect epistasis using incomplete information summary, and have proven it not only successfully let consistency of evidence, but also increase the power compared with traditional method (Detailed tutorial is shown in website).
	"""
	
	cran = "etma" 

	version("1.1-1", md5="1bd79576a49177b7e68396a36c3b4fca")

	depends_on("r@2.10:", type=("build", "run"))
