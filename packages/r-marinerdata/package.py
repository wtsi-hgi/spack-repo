# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarinerdata(RPackage):
	"""ExperimentHub data for the mariner package

	Subsampled Hi-C in HEK cells expressing the NHA9 fusion with an F to S mutated IDR ("FS") or without any mutations to the IDR ("Wildtype" or "WT"). These files are used for testing mariner functions and some examples.
	"""
	
	bioc = "marinerData"

	version("1.8.0", commit="5cadf8a7bb8d439d9943acbaf73b778b74e88d61")
	version("1.2.0", commit="2607746f1f2412ef2ff92623f582ccf6af441781")

	depends_on("r-experimenthub", type=("build", "run"))

