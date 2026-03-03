# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmdata(RPackage):
	"""Preparation, Checking and Post-Processing Data for PK/PD
Modeling

	Efficient tools for preparation, checking and post-processing of data in PK/PD (pharmacokinetics/pharmacodynamics) modeling, with focus on use of Nonmem. Attention is paid to ensure consistency, traceability, and Nonmem compatibility of Data. Rigorously checks final Nonmem datasets. Implemented in 'data.table', but easily integrated with 'base' and 'tidyverse'.
	"""
	
	homepage = "https://philipdelff.github.io/NMdata/"
	cran = "NMdata" 

	version("0.1.5", md5="b588926efda51be1e6d68dcc3c6d0f31")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
