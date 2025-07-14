# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMudata(RPackage):
	"""Serialization for MultiAssayExperiment Objects

	Save MultiAssayExperiments to h5mu files supported by muon and mudata. Muon is a Python framework for multimodal omics data analysis. It uses an HDF5-based format for data storage.
	"""
	
	homepage = "https://github.com/ilia-kats/MuData"
	bioc = "MuData"

	version("1.12.0", commit="9f7e2fde6f057f6033d5c6d4e7ba724d27f791fe")
	version("1.6.0", commit="42a68dd15c0acc2384c63680d741d927c8fbbc7c")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
