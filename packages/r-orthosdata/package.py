# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthosdata(RPackage):
	"""Data for the orthos package

	`orthosData` is the companion ExperimentData package to the `orthos` R package for mechanistic studies using differential gene expression experiments. It provides functions for retrieval from ExperimentHub and local caching of the models and datasets used internally in orthos.
	"""
	
	homepage = "https://github.com/fmicompbio/orthosData"
	bioc = "orthosData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/orthosData_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/orthosData/orthosData_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="631be84ad27eea65697c93a491fa96afcde226e05876cb9d644940d5dd9e3b59")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

