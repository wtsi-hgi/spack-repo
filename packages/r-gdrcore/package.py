# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrcore(RPackage):
	"""Processing functions and interface to process and analyze drug dose-response data

	This package contains core functions to process and analyze drug response data. The package provides tools for normalizing, averaging, and calculation of gDR metrics data. All core functions are wrapped into the pipeline function allowing analyzing the data in a straightforward way.
	"""
	
	bioc = "gDRcore" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gDRcore_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gDRcore/gDRcore_1.0.1.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.1", sha256="8c4660fe598c52ce80f16f0aae4e3751ccef6cec0802a2c3bef2acba6000fa25")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bumpymatrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-gdrutils@0.99.28:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
