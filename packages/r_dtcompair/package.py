# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtcompair(RPackage):
	"""Comparison of Binary Diagnostic Tests in a Paired Study Design

	Comparison of the accuracy of two binary diagnostic tests in a "paired" study design, i.e. when each test is applied to each subject in the study.
	"""
	
	homepage = "https://github.com/chstock/DTComPair"
	cran = "DTComPair" 

	version("1.2.2", md5="d2d3f50be5ae51bca77e9c888371bb15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-propcis", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
