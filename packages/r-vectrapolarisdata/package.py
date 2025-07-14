# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVectrapolarisdata(RPackage):
	"""Vectra Polaris and Vectra 3 multiplex single-cell imaging data

	Provides two multiplex imaging datasets collected on Vectra instruments at the University of Colorado Anschutz Medical Campus. Data are provided as a Spatial Experiment objects. Data is provided in tabular form and has been segmented and phenotyped using Inform software. Raw .tiff files are not included.
	"""
	
	homepage = "https://github.com/julia-wrobel/VectraPolarisData"
	bioc = "VectraPolarisData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/VectraPolarisData_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/VectraPolarisData/VectraPolarisData_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="1ca3951634ce5cf0b10dd9718adafa66fbbe7eaa5a7ecf8ed7c50ce91f26297f")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

