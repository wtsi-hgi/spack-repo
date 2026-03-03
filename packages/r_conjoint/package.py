# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConjoint(RPackage):
	"""An Implementation of Conjoint Analysis Method

	This is a simple R package that allows to measure the stated preferences using traditional conjoint analysis method.
	"""
	
	homepage = "www.r-project.org"
	cran = "conjoint" 

	version("1.41", md5="28bead35b49e74131dc2b1af9595b5de")

	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
