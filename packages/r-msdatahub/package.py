# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsdatahub(RPackage):
	"""Mass Spectrometry Data on ExperimentHub

	The MsDataHub package uses the ExperimentHub infrastructure to distribute raw mass spectrometry data files, peptide spectrum matches or quantitative data from proteomics and metabolomics experiments.
	"""
	
	homepage = "https://rformassspectrometry.github.io/MsDataHub"
	bioc = "MsDataHub"

	version("1.8.0", commit="a7636afa9b132a87c3af5123416c04aba3f8ce53")
	version("1.2.0", commit="5e1428493de47020c35318e25a37c4de88b8a80e")

	depends_on("r-experimenthub", type=("build", "run"))
