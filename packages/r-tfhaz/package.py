# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfhaz(RPackage):
	"""Transcription Factor High Accumulation Zones

	It finds trascription factor (TF) high accumulation DNA zones, i.e., regions along the genome where there is a high presence of different transcription factors. Starting from a dataset containing the genomic positions of TF binding regions, for each base of the selected chromosome the accumulation of TFs is computed. Three different types of accumulation (TF, region and base accumulation) are available, together with the possibility of considering, in the single base accumulation computing, the TFs present not only in that single base, but also in its neighborhood, within a window of a given width. Two different methods for the search of TF high accumulation DNA zones, called "binding regions" and "overlaps", are available. In addition, some functions are provided in order to analyze, visualize and compare results obtained with different input parameters.
	"""
	
	bioc = "TFHAZ" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TFHAZ_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TFHAZ/TFHAZ_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="91e2a2e09124bc2b0a67f2e328cd639c785e5e77fcc46d8a17599b67548b0401")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-orfik", type=("build", "run"))
