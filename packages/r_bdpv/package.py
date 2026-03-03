# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdpv(RPackage):
	"""Inference and Design for Predictive Values in Diagnostic Tests

	Computation of asymptotic confidence intervals for negative and positive predictive values in binary diagnostic tests in case-control studies. Experimental design for hypothesis tests on predictive values.
	"""
	
	cran = "bdpv" 

	version("1.3", md5="e1200a0ead29fe3baa859bcfb8b23661")

