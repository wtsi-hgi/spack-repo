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

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="53465316e53344432ca14ea72e0ff49a034e557af6202361b171dd9362c6bb41")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rgenometracksdata", type=("build", "run"))
