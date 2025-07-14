# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikein(RPackage):
	"""Affymetrix Spike-In Experiment Data

	Contains the HGU133 and HGU95 spikein experiment data.
	"""
	
	homepage = "https://bioconductor.org/packages/SpikeIn"
	bioc = "SpikeIn"

	version("1.50.0", commit="3d0c595e34a371c4d7483c09bfedc498be54bc70")
	version("1.44.0", commit="5dc4781787ef039ff5f5dad22f5eee93138e92d8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

