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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/synaptome.data_0.99.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/synaptome.data/synaptome.data_0.99.6.tar.gz"]

	version("0.99.6", tag="RELEASE_3_21")
	version("0.99.6", sha256="e5f1aca6946c3f75fcd6df798a792e72e20b11a3dd72163d065f7b6e407f9801")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

