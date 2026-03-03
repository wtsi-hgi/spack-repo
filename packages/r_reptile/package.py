# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReptile(RPackage):
	"""Regulatory DNA Element Prediction

	Predicting regulatory DNA elements based on epigenomic signatures. This package is more of a set of building blocks than a direct solution. REPTILE regulatory prediction pipeline is built on this R package. See <https://github.com/yupenghe/REPTILE> for more information.
	"""
	
	homepage = "https://github.com/yupenghe/REPTILE"
	cran = "REPTILE" 

	version("1.0", md5="1270a1ad6638f5e9204b07d1a7e22da1")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-optparse@1.3.2:", type=("build", "run"))
	depends_on("r-randomforest@4.6.12:", type=("build", "run"))
	depends_on("r-flux@0.3.0:", type=("build", "run"))
