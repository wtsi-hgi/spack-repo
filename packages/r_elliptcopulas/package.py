# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElliptcopulas(RPackage):
	"""Inference of Elliptical Distributions and Copulas

	Provides functions for the simulation and
  the nonparametric estimation of elliptical distributions,
  meta-elliptical copulas and trans-elliptical distributions,
  following the article Derumigny and Fermanian (2022) <doi:10.1016/j.jmva.2022.104962>.
	"""
	
	homepage = "https://github.com/AlexisDerumigny/ElliptCopulas"
	cran = "ElliptCopulas" 

	version("0.1.3", md5="66c0e6efd0187352ef6847e2101a38be")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-runuran", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
