# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfa(RPackage):
	"""Configural Frequency Analysis (CFA)

	Analysis of configuration frequencies for simple and repeated measures, multiple-samples CFA, hierarchical CFA, bootstrap CFA, functional CFA, Kieser-Victor CFA, and Lindner's test using a conventional and an accelerated algorithm.
	"""
	
	cran = "cfa" 

	version("0.10-1", md5="6fdcb12063b87319d75dbbfc4cedf108")

	depends_on("r@3.0.1:", type=("build", "run"))
