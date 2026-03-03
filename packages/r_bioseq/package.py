# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioseq(RPackage):
	"""A Toolbox for Manipulating Biological Sequences

	Classes and functions to work with biological sequences (DNA, RNA and amino acid sequences).
    Implements S3 infrastructure to work with biological sequences as described in Keck (2020) <doi:10.1111/2041-210X.13490>.
    Provides a collection of functions to perform biological conversion among classes
    (transcription, translation) and basic operations on sequences
    (detection, selection and replacement based on positions or patterns).
    The package also provides functions to import and export sequences from and to other package formats.
	"""
	
	homepage = "https://fkeck.github.io/bioseq/"
	cran = "bioseq" 

	version("0.1.4", md5="7fdcd24f230922484d291349909cd600")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
