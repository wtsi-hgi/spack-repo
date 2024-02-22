# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStat2data(RPackage):
	"""Datasets for Stat2

	Datasets for the textbook Stat2: Modeling with Regression and ANOVA (second edition). 
    The package also includes data for the first edition, Stat2: Building Models for a World of Data
    and a few functions for plotting diagnostics.
	"""
	
	homepage = "https://github.com/statmanrobin/Stat2Data"
	cran = "Stat2Data" 

	version("2.0.0", md5="9716c4c61a593a257824b4096ec9c2f9")

	depends_on("r@2.10:", type=("build", "run"))
