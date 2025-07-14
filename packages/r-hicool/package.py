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

	version("1.8.0", commit="59a6b9c0828cdde5aca661a28e2954c7a04da2ae")
	version("1.2.0", commit="7fe5520c59574095b80341d4db3113cece0a2fec")

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
