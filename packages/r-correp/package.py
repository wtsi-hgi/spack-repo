# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrep(RPackage):
	"""Multivariate Correlation Estimator and Statistical Inference Procedures.

	Multivariate correlation estimation and statistical inference. See package vignette.
	"""
	
	bioc = "CORREP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CORREP_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CORREP/CORREP_1.68.0.tar.gz"]

	version("1.68.0", md5="2cf1b0a377be4fec857415e908e2d8d2")

	depends_on("r-e1071", type=("build", "run"))
