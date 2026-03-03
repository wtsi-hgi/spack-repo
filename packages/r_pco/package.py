# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPco(RPackage):
	"""Panel Cointegration Tests

	Computation of the Pedroni (1999) panel cointegration test statistics.  Reported are the empirical and the standardized values. 
	"""
	
	cran = "pco" 

	version("1.0.1", md5="e435dff7919b4f4cf55303755fe06cda")

