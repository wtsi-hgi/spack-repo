# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynaptomeData(RPackage):
	"""AnnotationData for Synaptome.DB package

	The package provides access to the copy of the Synaptic proteome database. It was designed as an accompaniment for Synaptome.DB package. Database provides information for specific synaptic genes and allows building the protein-protein interaction graph for gene sets, synaptic compartments, and brain regions. In the current update we added 6 more synaptic proteome studies, which resulted in total of 64 studies. We introduced Synaptic Vesicle as a separate compartment. We also added coding mutations for Autistic Spectral disorder and Epilepsy collected from publicly available databases.
	"""
	
	bioc = "synaptome.data"

	version("0.99.6", commit="0a8f3a9e1661864691d8848f78450a6781859898")
	version("0.99.6", commit="0a8f3a9e1661864691d8848f78450a6781859898")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

