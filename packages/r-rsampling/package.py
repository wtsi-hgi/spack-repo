# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsampling(RPackage):
	"""Ports the Workflow of "Resampling Stats" Add-in to R

	Resampling Stats (http://www.resample.com) is an add-in for
    running randomization tests in Excel worksheets. The workflow is (1) to define
    a statistic of interest that can be calculated from a data table, (2) to
    randomize rows ad/or columns of a data table to simulate a null hypothesis
    and (3) and to score the value of the statistic from many randomizations. The
    relative frequency distribution of the statistic in the simulations is then
    used to infer the probability of the observed value be generated by the null
    process (probability of Type I error). This package intends to translate this
    logic for R for teaching purposes. Keeping the original workflow is favored over
    performance.
	"""
	
	cran = "Rsampling" 

	version("0.1.1", md5="a170a6c816a27ec0f2b5f7f51232f7df")

	depends_on("r@3:", type=("build", "run"))
