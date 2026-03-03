# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDramaanalysis(RPackage):
	"""Analysis of Dramatic Texts

	Analysis of preprocessed dramatic texts, with respect to literary research. 
  The package provides functions to analyze and visualize information about characters,
  stage directions, the dramatic structure and the text itself.
  The dramatic texts are expected to be in CSV format, which can be installed from within 
  the package, sample texts are provided. The package and the reasoning behind it are described in 
  Reiter et al. (2017) <doi:10.18420/in2017_119>.
	"""
	
	homepage = "https://github.com/quadrama/DramaAnalysis"
	cran = "DramaAnalysis" 

	version("3.0.2", md5="1963eda85733e91751bcce6e2e299958")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-git2r@0.24:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-tokenizers@0.2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
