# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDam(RPackage):
	"""Data Analysis Metabolomics

	A collection of functions which aim to assist common computational workflow for analysis of matabolomic data..
	"""
	
	cran = "dam" 

	version("0.0.1", md5="aa444780e82c55a297bdd11552d0fbfd")

	depends_on("r@3.2.3:", type=("build", "run"))
