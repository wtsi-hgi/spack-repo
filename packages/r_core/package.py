# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCore(RPackage):
	"""Cores of Recurrent Events

	Given a collection of intervals with integer start and end 
    positions, find recurrently targeted regions and estimate the significance 
    of finding. Randomization is implemented by parallel methods, either 
    using local host machines, or submitting grid engine jobs.
	"""
	
	cran = "CORE" 

	version("3.2", md5="ccc1ebd995e924f333108dc84fb2a091")

