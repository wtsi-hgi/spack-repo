# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrd(RPackage):
	"""Transmission Ratio Distortion

	Transmission Ratio Distortion (TRD) is a genetic phenomenon where the two alleles from either parent are not transmitted to the offspring at the expected 1:1 ratio under Mendelian inheritance, leading to spurious signals in genetic association studies. Functions in this package are developed to account for this phenomenon using loglinear model and Transmission Disequilibrium Test (TDT). Some population information can also be calculated.
	"""
	
	cran = "TRD" 

	version("1.1", md5="99f127ef7a529ee07a7bdd9d3df3dd49")

	depends_on("r-rlab@2.15.1:", type=("build", "run"))
