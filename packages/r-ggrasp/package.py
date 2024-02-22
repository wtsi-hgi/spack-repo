# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrasp(RPackage):
	"""Gaussian-Based Genome Representative Selector with
Prioritization

	Given a group of genomes and their relationship with each other, the package clusters the genomes and selects the most representative members of each cluster. Additional data can be provided to the prioritize certain genomes. The results can be printed out as a list or a new phylogeny with graphs of the trees and distance distributions also available. For detailed introduction see: Thomas H Clarke, Lauren M Brinkac, Granger Sutton, and Derrick E Fouts (2018), GGRaSP: a R-package for selecting representative genomes using Gaussian mixture models, Bioinformatics, bty300, <doi:10.1093/bioinformatics/bty300>.
	"""
	
	cran = "ggrasp" 

	version("1.2", md5="a4ffca12b051ec20e799c5ffb3f0a124")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bgmm", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
