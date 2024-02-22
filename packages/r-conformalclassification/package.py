# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalclassification(RPackage):
	"""Transductive and Inductive Conformal Predictions for
Classification Problems

	Implementation of transductive conformal prediction (see Vovk, 2013, <doi:10.1007/978-3-642-41142-7_36>) and inductive conformal prediction (see Balasubramanian et al., 2014, ISBN:9780124017153) for classification problems.
	"""
	
	cran = "conformalClassification" 

	version("1.0.0", md5="2cc2c1d1ebe2d83489dae4e9cb261f8f")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
