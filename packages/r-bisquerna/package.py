# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisquerna(RPackage):
	"""Decomposition of Bulk Expression with Single-Cell Sequencing

	Provides tools to accurately estimate cell type abundances 
    from heterogeneous bulk expression. A reference-based method utilizes
    single-cell information to generate a signature matrix and transformation
    of bulk expression for accurate regression based estimates. A marker-based
    method utilizes known cell-specific marker genes to measure relative
    abundances across samples.
    For more details, see Jew and Alvarez et al (2019) <doi:10.1101/669911>.
	"""
	
	homepage = "https://www.biorxiv.org/content/10.1101/669911v1"
	cran = "BisqueRNA" 

	version("1.0.5", md5="a9226ff04e21bfc97fc707f4e11d8a06")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
