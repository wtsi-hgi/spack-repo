# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlinefdr(RPackage):
	"""Online error rate control

	This package allows users to control the false discovery rate (FDR) or familywise error rate (FWER) for online multiple hypothesis testing, where hypotheses arrive in a stream. In this framework, a null hypothesis is rejected based on the evidence against it and on the previous rejection decisions.
	"""
	
	homepage = "https://dsrobertson.github.io/onlineFDR/index.html"
	bioc = "onlineFDR"

	version("2.16.0", commit="62cfe20b535b068801ec4fc7e856400ce3acbeb5")
	version("2.10.0", commit="c52a623040d5bf2492a2c24af794388492510302")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
