# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromplot(RPackage):
	"""Global visualization tool of genomic data

	Package designed to visualize genomic data along the chromosomes, where the vertical chromosomes are sorted by number, with sex chromosomes at the end.
	"""
	
	bioc = "chromPlot" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/chromPlot_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/chromPlot/chromPlot_1.30.0.tar.gz"]

	version("1.30.0", sha256="fee0aa9c4fa3ff8c82d06192897a9928491f45157056583d2f19bf98028d18f7")

	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
