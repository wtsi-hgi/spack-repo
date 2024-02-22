# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChords(RPackage):
	"""Estimation in Respondent Driven Samples

	Maximum likelihood estimation in respondent driven samples.
	"""
	
	cran = "chords" 

	version("0.95.4", md5="e07fed2b6142962bfbcfaaef50bf9e14")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
