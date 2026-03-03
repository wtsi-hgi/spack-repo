# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSs3sim(RPackage):
	"""Fisheries Stock Assessment Simulation Testing with Stock
Synthesis

	Develops a framework for fisheries stock assessment simulation
    testing with Stock Synthesis (SS) as described in Anderson et al.
    (2014) <doi:10.1371/journal.pone.0092725>.
	"""
	
	homepage = "https://github.com/ss3sim/ss3sim"
	cran = "ss3sim" 

	version("1.0.3", md5="7a4452fa0c1a2d666825f3dfa3471ceb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-r4ss@1.35:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
