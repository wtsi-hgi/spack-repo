# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancerinsilico(RPackage):
	"""An R interface for computational modeling of tumor progression

	The CancerInSilico package provides an R interface for running mathematical models of tumor progresson and generating gene expression data from the results. This package has the underlying models implemented in C++ and the output and analysis features implemented in R.
	"""
	
	bioc = "CancerInSilico" 

	version("2.22.0", commit="c5431f1c47c9b88ed68778a41c025d377b785146")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
