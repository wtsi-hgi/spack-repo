# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcrank(RPackage):
	"""Predicting binding site consensus from ranked DNA sequences

	Functions and classes for de novo prediction of transcription factor binding consensus by heuristic search
	"""
	
	bioc = "BCRANK"

	version("1.70.0", commit="6712d80246422a20a6f8ae46cf65a34bf62792c3")
	version("1.64.0", commit="e80fdd5ec2c7d33b971f7f4528b3837ad8dd3fd3")

	depends_on("r-biostrings", type=("build", "run"))
