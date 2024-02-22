# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsmn(RPackage):
	"""Truncated Scale Mixtures of Normal Distributions

	Return the first four moments of the SMN distributions (Normal, Student-t, Pearson VII, Slash or Contaminated Normal).
	"""
	
	cran = "TSMN" 

	version("1.0.0", md5="478f6b9626c432f43357a31efa638495")

