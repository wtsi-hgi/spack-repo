# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpsychor(RPackage):
	"""Modern Psychometrics with R

	Supplementary materials and datasets for the book "Modern Psychometrics With R" (Mair, 2018, Springer useR! series).
	"""
	
	cran = "MPsychoR" 

	version("0.10-8", md5="1a26dc3d28050f75e915b871b9eb7079")

	depends_on("r@3.0.2:", type=("build", "run"))
