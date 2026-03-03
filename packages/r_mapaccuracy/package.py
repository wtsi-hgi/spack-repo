# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapaccuracy(RPackage):
	"""Unbiased Thematic Map Accuracy and Area

	Unbiased estimators of overall and per-class thematic map accuracy and area published in Olofsson et al. (2014) <doi:10.1016/j.rse.2014.02.015> and Stehman (2014) <doi:10.1080/01431161.2014.930207>.
	"""
	
	cran = "mapaccuracy" 

	version("0.1.2", md5="52a4e230e6b7a9348c19e004d5bd0723")
	version("0.1.1", md5="67da163684689cd5aaca14e3487f8a30")

	depends_on("r@3:", type=("build", "run"))
