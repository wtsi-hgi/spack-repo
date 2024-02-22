# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNot(RPackage):
	"""Narrowest-Over-Threshold Change-Point Detection

	Provides efficient implementation of the Narrowest-Over-Threshold methodology for detecting an unknown number of change-points occurring at unknown locations in one-dimensional data following 'deterministic signal + noise' model. Currently implemented scenarios are: piecewise-constant signal, piecewise-constant signal with a heavy-tailed noise, piecewise-linear signal, piecewise-quadratic signal, piecewise-constant signal and with piecewise-constant variance of the noise. For details, see Baranowski, Chen and Fryzlewicz (2019) <doi:10.1111/rssb.12322>.
	"""
	
	cran = "not" 

	version("1.5", md5="d8054973140b011120370257f03d4e7f")

