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

	version("1.68.0", commit="fc3535492b893027b457a5fa7e93dbea87a82db4")

	depends_on("r-e1071", type=("build", "run"))
