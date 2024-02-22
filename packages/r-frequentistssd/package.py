# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrequentistssd(RPackage):
	"""Screened Selection Design with Survival Endpoints

	A study based on the screened selection design (SSD) is an exploratory phase II randomized trial with two or more arms but without concurrent control. The primary aim of the SSD trial is to pick a desirable treatment arm (e.g., in terms of the median survival time) to recommend to the subsequent randomized phase IIb (with the concurrent control) or phase III. Though The survival endpoint is often encountered in phase II trials, the existing SSD methods cannot deal with the survival endpoint. Furthermore, the existing SSD won’t control the type I error rate.  The proposed designs can “partially” control or provide the empirical type I error/false positive rate by an optimal algorithm (implemented by the optimal() function) for each arm. All the design needed components (sample size, operating characteristics) are supported.
	"""
	
	cran = "frequentistSSD" 

	version("0.1.1", md5="21dfb3d4005a19837fd2fd1ec27f87d3")

	depends_on("r-survival", type=("build", "run"))
