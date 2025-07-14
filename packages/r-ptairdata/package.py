# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtairdata(RPackage):
	"""PTR-TOF-MS volatolomics raw datasets from exhaled air and cell culture headspace

	The package ptairData contains two raw datasets from Proton-Transfer-Reaction Time-of-Flight mass spectrometer acquisitions (PTR-TOF-MS), in the HDF5 format. One from the exhaled air of two volunteer healthy individuals with three replicates, and one from the cell culture headspace from two mycobacteria species and one control (culture medium only) with two replicates. Those datasets are used in the examples and in the vignette of the ptairMS package (PTR-TOF-MS data pre-processing). There are also used to gererate the ptrSet in the ptairMS data : exhaledPtrset and mycobacteriaSet
	"""
	
	bioc = "ptairData"

	version("1.16.0", commit="ad6240f5557a38360b4066b9cd2a4d3f9442093e")
	version("1.10.0", commit="8d2c280297ea52537c9bc288a8eec8f2083c0248")

	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))

