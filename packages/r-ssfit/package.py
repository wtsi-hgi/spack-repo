# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsfit(RPackage):
	"""Fitting of Parametric Models using Summary Statistics

	Fits complex parametric models using the method proposed by Cox and Kartsonaki (2012) without likelihoods.
	"""
	
	cran = "ssfit" 

	version("1.2", md5="31a2fac475fe42eb84969f54afad5c6a")

	depends_on("r-survey", type=("build", "run"))
