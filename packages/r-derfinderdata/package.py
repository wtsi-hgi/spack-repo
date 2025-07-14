# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderdata(RPackage):
	"""Processed BigWigs from BrainSpan for examples

	Processed 22 samples from BrainSpan keeping only the information for chromosome 21. Data is stored in the BigWig format and is used for examples in other packages.
	"""
	
	homepage = "https://github.com/leekgroup/derfinderData"
	bioc = "derfinderData"

	version("2.26.0", commit="1b44e6b7cad938e4e0d79f538019b5088bb8eddd")
	version("2.20.0", commit="4fdeff7e9ef1ae00708b19cc3f28e733755a286e")

	depends_on("r@3.5:", type=("build", "run"))

