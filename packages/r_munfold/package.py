# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMunfold(RPackage):
	"""Metric Unfolding

	Multidimensional unfolding using Schoenemann's algorithm for metric
   and Procrustes rotation of unfolding results.
	"""
	
	homepage = "http://www.elff.eu/software/munfold/"
	cran = "munfold" 

	version("0.3.5", md5="9d66be6b416f456ed72e8d18ca324ff9")

	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
