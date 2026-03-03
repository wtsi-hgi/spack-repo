# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfer(RPackage):
	"""Forensic Glass Transfer Probabilities

	Statistical interpretation of forensic glass transfer (Simulation of the probability distribution of recovered glass fragments).
	"""
	
	cran = "tfer" 

	version("1.3", md5="cc4cafba3da51822f39a2b3e484331c4")

