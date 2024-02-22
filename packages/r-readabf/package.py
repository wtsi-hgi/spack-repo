# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadabf(RPackage):
	"""Loads Axon Binary Files

	Loads Axon Binary Files (both 'ABF' and 'ABF2') created by Axon Instruments/Molecular Devices software such as 'pClamp'.
	"""
	
	cran = "readABF" 

	version("1.0.2", md5="f82f72538a6b5b418313b6d4dff4377f")

	depends_on("r@3.2:", type=("build", "run"))
