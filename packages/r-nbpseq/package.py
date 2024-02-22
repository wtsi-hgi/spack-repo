# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbpseq(RPackage):
	"""Negative Binomial Models for RNA-Sequencing Data

	Negative Binomial (NB) models for two-group comparisons and
    regression inferences from RNA-Sequencing Data.
	"""
	
	cran = "NBPSeq" 

	version("0.3.1", md5="a4d8aa40ae37d798b2f8d711902aa953")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
