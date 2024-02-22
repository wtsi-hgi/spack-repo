# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankicc(RPackage):
	"""Rank Intraclass Correlation for Clustered Data

	Estimates the rank intraclass correlation coefficient (ICC) for clustered continuous and ordinal data. See Tu et al. (2023) <DOI:10.1002/sim.9864> for details. 
	"""
	
	cran = "rankICC" 

	version("1.0.2", md5="2f31371b021d58f0eea71d6bce2bb545")

