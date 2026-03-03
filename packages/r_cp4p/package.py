# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCp4p(RPackage):
	"""Calibration Plot for Proteomics

	Functions to check whether a vector of p-values respects the assumptions of FDR (false discovery rate) control procedures and to compute adjusted p-values.
	"""
	
	cran = "cp4p" 

	version("0.3.6", md5="aa8dd7516b7a24d177515525c0eead19")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
