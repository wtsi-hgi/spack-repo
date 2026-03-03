# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaipe(RPackage):
	"""Graphical Extension with Accuracy in Parameter Estimation
(GAIPE)

	Implements graphical extension with accuracy in parameter estimation (AIPE) on RMSEA for sample size planning in structural equation modeling based on Lin, T.-Z. & Weng, L.-J. (2014) <doi: 10.1080/10705511.2014.915380>. And, it can also implement AIPE on RMSEA and power analysis on RMSEA.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "GAIPE" 

	version("1.1", md5="2c1e77d6e247d553b2e67759610eb457")

	depends_on("r@3.4.1:", type=("build", "run"))
