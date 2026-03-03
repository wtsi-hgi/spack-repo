# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSenspe(RPackage):
	"""Estimating Specificity at Controlled Sensitivity, or Vice Versa

	Perform biomarker evaluation and comparison in terms of specificity at a controlled sensitivity level, or sensitivity at a controlled specificity level. Point estimation and exact bootstrap of Huang, Parakati, Patil, and Sanda (2023) <doi:10.5705/ss.202021.0020> for the one- and two-biomarker problems are implemented.
	"""
	
	cran = "SenSpe" 

	version("1.3", md5="79a2d4e99a7a9ed53d5353c882e2c67d")

	depends_on("r@2.8:", type=("build", "run"))
