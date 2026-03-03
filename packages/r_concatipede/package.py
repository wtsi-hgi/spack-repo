# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcatipede(RPackage):
	"""Easy Concatenation of Fasta Sequences

	Concatenation of multiple sequence alignments based on a
    correspondence table that can be edited in Excel <doi:10.5281/zenodo.5130603>.
	"""
	
	homepage = "https://github.com/tardipede/concatipede"
	cran = "concatipede" 

	version("1.0.1", md5="7addefb87aefa274c396ef1822670944")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qualv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
