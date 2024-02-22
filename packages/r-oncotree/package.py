# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncotree(RPackage):
	"""Estimating Oncogenetic Trees

	Construct and evaluate directed tree structures that
   model the process of occurrence of genetic alterations during carcinogenesis
   as described in Szabo, A. and Boucher, K (2002)  <doi:10.1016/S0025-5564(02)00086-X>.
	"""
	
	homepage = "https://github.com/anikoszabo/Oncotree"
	cran = "Oncotree" 

	version("0.3.5", md5="8cf5104fe6d0da2863bf080de2c577fe")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
