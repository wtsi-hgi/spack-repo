# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonotonehazardratio(RPackage):
	"""Nonparametric Estimation and Inference of a Monotone Hazard
Ratio Function

	A tool for nonparametric estimation and inference of a non-decreasing monotone hazard
    ratio from a right censored survival dataset.  The
    estimator is based on a generalized Grenander typed estimator, and the
    inference procedure relies on direct plugin estimation of a first order derivative.  More
    details please refer to the paper "Nonparametric inference under a monotone
    hazard ratio order" by Y. Wu and T. Westling (2022) <arXiv:2205.01745>.
	"""
	
	homepage = "https://github.com/Yujian-Wu/MonotoneHazardRatio"
	cran = "MonotoneHazardRatio" 

	version("0.1.1", md5="99fa7a7a775655e66c26877c94b17555")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-twostagete", type=("build", "run"))
