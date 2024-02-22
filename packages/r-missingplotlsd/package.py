# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissingplotlsd(RPackage):
	"""Missing Plot in LSD

	A system for Analysis of LSD when there is one missing observation. Methods for this process is described in A.M.Gun,M.K.Gupta,B.Dasgupta(2019,ISBN:81-87567-81-3).
	"""
	
	cran = "MissingPlotLSD" 

	version("0.1.0", md5="fa60eb88ff808ed25bf0b809df503e6a")

