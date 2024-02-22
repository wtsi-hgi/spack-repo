# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypr(RPackage):
	"""Hypothesis Matrix Translation

	Translation between experimental null hypotheses, hypothesis matrices, and contrast matrices as used in linear regression models. The package is based on the method described in Schad et al. (2019) <doi:10.1016/j.jml.2019.104038> and Rabe et al. (2020) <doi:10.21105/joss.02134>.
	"""
	
	homepage = "https://maxrabe.com/hypr"
	cran = "hypr" 

	version("0.2.8", md5="f73a40ab080292cea81646d56b3d011e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
