# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStylo(RPackage):
	"""Stylometric Multivariate Analyses

	Supervised and unsupervised multivariate methods, supplemented by GUI and some visualizations, to perform various analyses in the field of computational stylistics, authorship attribution, etc. For further reference, see Eder et al. (2016), <https://journal.r-project.org/archive/2016/RJ-2016-007/index.html>. You are also encouraged to visit the Computational Stylistics Group's website <https://computationalstylistics.github.io/>, where a reasonable amount of information about the package and related projects are provided.
	"""
	
	homepage = "https://github.com/computationalstylistics/stylo"
	cran = "stylo" 

	version("0.7.4", md5="3111a0df7c49809b5ea6f2db752a5d43")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-tsne", type=("build", "run"))
