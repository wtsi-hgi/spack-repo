# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcellviper(RPackage):
	"""Human B-cell transcriptional interactome and normal human B-cell expression data

	This package provides a human B-cell context-specific transcriptional regulatory network and a human normal B-cells dataset for the examples in package viper.
	"""
	
	bioc = "bcellViper" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bcellViper_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/bcellViper/bcellViper_1.38.0.tar.gz"]

	version("1.38.0", sha256="1009f48b1b743005ede62ebac66f95554df2db33d37298ed2998ba017e7931e1")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

