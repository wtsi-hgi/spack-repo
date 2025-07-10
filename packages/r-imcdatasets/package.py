# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImcdatasets(RPackage):
	"""Collection of publicly available imaging mass cytometry (IMC) datasets

	The imcdatasets package provides access to publicly available IMC datasets. IMC is a technology that enables measurement of > 40 proteins from tissue sections. The generated images can be segmented to extract single cell data. Datasets typically consist of three elements: a SingleCellExperiment object containing single cell data, a CytoImageList object containing multichannel images and a CytoImageList object containing the cell masks that were used to extract the single cell data from the images.
	"""
	
	homepage = "https://github.com/BodenmillerGroup/imcdatasets"
	bioc = "imcdatasets" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/imcdatasets_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/imcdatasets/imcdatasets_1.10.0.tar.gz"]

	version("1.10.0", sha256="faf6b82b47daca4c6661668a6fdee0dbe864db19ff962f62724bf5d7318a717b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-cytomapper", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))

