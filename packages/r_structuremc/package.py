# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructuremc(RPackage):
	"""Structured Matrix Completion

	Provides an efficient method to recover the missing block of an approximately low-rank matrix. Current literature on matrix completion focuses primarily on independent sampling models under which the individual observed entries are sampled independently. Motivated by applications in genomic data integration, we propose a new framework of structured matrix completion (SMC) to treat structured missingness by design [Cai T, Cai TT, Zhang A (2016) <doi:10.1080/01621459.2015.1021005>]. Specifically, our proposed method aims at efficient matrix recovery when a subset of the rows and columns of an approximately low-rank matrix are observed. The main function in our package, smc.FUN(), is for recovery of the missing block A22 of an approximately low-rank matrix A given the other blocks A11, A12, A21.
	"""
	
	cran = "StructureMC" 

	version("1.0", md5="0e82c51d2188453a416b5c84c7a8a31b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
