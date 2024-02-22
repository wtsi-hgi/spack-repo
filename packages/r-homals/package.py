# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomals(RPackage):
	"""Gifi Methods for Optimal Scaling

	Performs a homogeneity analysis (multiple correspondence analysis) and various extensions. Rank restrictions on the category quantifications can be imposed (nonlinear PCA). The categories are transformed by means of optimal scaling with options for nominal, ordinal, and numerical scale levels (for rank-1 restrictions). Variables can be grouped into sets, in order to emulate regression analysis and canonical correlation analysis. 
	"""
	
	cran = "homals" 

	version("1.0-10", md5="4269a0c6f4aa9842db057fa059be179a")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
