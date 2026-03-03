# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAslib(RPackage):
	"""Interface to the Algorithm Selection Benchmark Library

	Provides an interface to the algorithm selection benchmark library
    at <http://www.aslib.net> and the 'LLAMA' package
    (<https://cran.r-project.org/package=llama>) for building
    algorithm selection models; see Bischl et al. (2016)
    <doi:10.1016/j.artint.2016.04.003>.
	"""
	
	homepage = "https://github.com/coseal/aslib-r/"
	cran = "aslib" 

	version("0.1.2", md5="eaf95e0fa8acfc452628c68e76e337c5")

	depends_on("r-batchtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-llama", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-paramhelpers", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
