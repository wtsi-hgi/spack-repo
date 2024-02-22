# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElectivity(RPackage):
	"""Algorithms for Electivity Indices

	Provides all electivity algorithms (including Vanderploeg and Scavia 
    electivity) that were examined in Lechowicz (1982) <doi:10.1007/BF00349007>, 
    plus the example data that were provided for moth resource utilisation.
	"""
	
	homepage = "https://github.com/DesiQuintans/electivity"
	cran = "electivity" 

	version("1.0.2", md5="983a4605e5cead00d934a1c84d97db2a")

	depends_on("r@3.4:", type=("build", "run"))
