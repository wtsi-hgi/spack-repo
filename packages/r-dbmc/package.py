# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbmc(RPackage):
	"""Confidence Interval for Matrix Completion via De-Biased
Estimator

	Implements the de-biased estimator for low-rank matrix completion and provides confidence intervals for entries of interest. See: by Chen et al. (2019) <doi:10.1073/pnas.1910053116>, Mai (2021) <arXiv:2103.11749>.
	"""
	
	cran = "dbMC" 

	version("1.0.0", md5="c4f27c71dda07961c4ef631fc977fa54")

	depends_on("r-softimpute", type=("build", "run"))
