# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicool(RPackage):
	"""HiCool

	HiCool provides an R interface to process and normalize Hi-C paired-end fastq reads into .(m)cool files. .(m)cool is a compact, indexed HDF5 file format specifically tailored for efficiently storing HiC-based data. On top of processing fastq reads, HiCool provides a convenient reporting function to generate shareable reports summarizing Hi-C experiments and including quality controls.
	"""
	
	homepage = "https://github.com/js2264/HiCool"
	bioc = "HiCool" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HiCool_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HiCool/HiCool_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="d2d6aaa5b81a1cd04b808b2b5544b62a92f75dd6f6e5492b1c559ecb85be9546")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-hicexperiment", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rmdformats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
