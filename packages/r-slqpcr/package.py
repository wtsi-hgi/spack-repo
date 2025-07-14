# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlqpcr(RPackage):
	"""Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH

	Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH
	"""
	
	bioc = "SLqPCR"

	version("1.74.0", commit="5dc208f3e9056bd18553817934a05e2d577e5df9")
	version("1.68.0", commit="1007225ca8aaf936f2676401b69da5c29cef0e24")

	depends_on("r@2.4:", type=("build", "run"))
