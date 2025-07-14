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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsDataHub_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsDataHub/MsDataHub_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="991de642121db86be31c55c72ad17ac24999afd66a1ec568636e8ff0d78cd30d")

	depends_on("r-experimenthub", type=("build", "run"))
