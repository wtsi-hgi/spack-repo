# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenometracks(RPackage):
	"""Integerated visualization of epigenomic data

	rGenomeTracks package leverages the power of pyGenomeTracks software with the interactivity of R. pyGenomeTracks is a python software that offers robust method for visualizing epigenetic data files like narrowPeak, Hic matrix, TADs and arcs, however though, here is no way currently to use it within R interactive session. rGenomeTracks wrapped the whole functionality of pyGenomeTracks with additional utilites to make to more pleasant for R users.
	"""
	
	bioc = "rGenomeTracks" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rGenomeTracks_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rGenomeTracks/rGenomeTracks_1.8.0.tar.gz"]

	version("1.8.0", md5="860c81f62e3abf51de44d4dcdcdbfeef")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rgenometracksdata", type=("build", "run"))
