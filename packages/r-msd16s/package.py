# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsd16s(RPackage):
	"""Healthy and moderate to severe diarrhea 16S expression data

	Gut 16S sequencing expression data from 992 healthy and moderate-to-severe diarrhetic samples used in 'Diarrhea in young children from low-income countries leads to large-scale alterations in intestinal microbiota composition'.
	"""
	
	homepage = "http://www.cbcb.umd.edu/research/projects/GEMS-pathogen-discovery"
	bioc = "msd16s" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/msd16s_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/msd16s/msd16s_1.22.0.tar.gz"]

	version("1.22.0", md5="fddb80467192bbe28bb92599941be5d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))

	# experiment