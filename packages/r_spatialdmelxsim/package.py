# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdmelxsim(RPackage):
	"""Spatial allelic expression counts for fly cross embryo

	Spatial allelic expression counts from Combs & Fraser (2018), compiled into a SummarizedExperiment object. This package contains data of allelic expression counts of spatial slices of a fly embryo, a Drosophila melanogaster x Drosophila simulans cross. See the CITATION file for the data source, and the associated script for how the object was constructed from publicly available data.
	"""
	
	homepage = "https://github.com/mikelove/spatialDmelxsim"
	bioc = "spatialDmelxsim" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/spatialDmelxsim_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/spatialDmelxsim/spatialDmelxsim_1.8.0.tar.gz"]

	version("1.8.0", md5="2fec38c7672022e76f2b7a7ba7b9a677")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

