# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotubes(RPackage):
	"""Mouse nanotube CAGE data

	Cap Analysis of Gene Expression (CAGE) data from "Identification of Gene Transcription Start Sites and Enhancers Responding to Pulmonary Carbon Nanotube Exposure in Vivo" by Bornholdt et al. supplied as CAGE Transcription Start Sites (CTSSs).
	"""
	
	homepage = "https://github.com/MalteThodberg/nanotubes"
	bioc = "nanotubes"

	version("1.24.0", commit="0b7ad6e6c4fbef80c1bf94a814f0abf1a0a7d4ba")
	version("1.18.0", commit="e56bc09da4d4b071e2a0010009d4ce4d4b83628e")

	depends_on("r@3.6:", type=("build", "run"))

