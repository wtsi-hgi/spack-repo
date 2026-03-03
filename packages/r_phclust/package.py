# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhclust(RPackage):
	"""Poisson Hurdle Clustering for Sparse Microbiome Data

	Clustering analysis for sparse microbiome data, based on a Poisson hurdle model.
	"""
	
	cran = "PHclust" 

	version("0.1.0", md5="c184e9437a4cb9305ec19341520c7473")

	depends_on("r@2.10:", type=("build", "run"))
