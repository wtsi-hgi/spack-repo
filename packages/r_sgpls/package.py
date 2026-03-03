# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgpls(RPackage):
	"""Sparse Group Partial Least Square Methods

	Regularized version of partial least square approaches providing sparse, group, and sparse group versions of partial least square regression models (Liquet, B., Lafaye de Micheaux, P., Hejblum B., Thiebaut, R. (2016) <doi:10.1093/bioinformatics/btv535>). Version of PLS Discriminant analysis is also provided.
	"""
	
	cran = "sgPLS" 

	version("1.8", md5="0d1a058c3f655358ee7fdbf3377c5326")

	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
