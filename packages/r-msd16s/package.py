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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/msd16s_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/msd16s/msd16s_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="b321b6ae241863d8108ad24b143c8794ace2d78508b9d982c85d78fa3a5beb68")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))

