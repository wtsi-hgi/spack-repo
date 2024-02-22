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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/VectraPolarisData_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/VectraPolarisData/VectraPolarisData_1.6.0.tar.gz"]

	version("1.6.0", md5="ea2006b85e374e76fbd70ca8b0819072")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

	# experiment