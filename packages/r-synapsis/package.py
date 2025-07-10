# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapsis(RPackage):
	"""An R package to automate the analysis of double-strand break repair during meiosis

	Synapsis is a Bioconductor software package for automated (unbiased and reproducible) analysis of meiotic immunofluorescence datasets. The primary functions of the software can i) identify cells in meiotic prophase that are labelled by a synaptonemal complex axis or central element protein, ii) isolate individual synaptonemal complexes and measure their physical length, iii) quantify foci and co-localise them with synaptonemal complexes, iv) measure interference between synaptonemal complex-associated foci. The software has applications that extend to multiple species and to the analysis of other proteins that label meiotic prophase chromosomes. The software converts meiotic immunofluorescence images into R data frames that are compatible with machine learning methods. Given a set of microscopy images of meiotic spread slides, synapsis crops images around individual single cells, counts colocalising foci on strands on a per cell basis, and measures the distance between foci on any given strand.
	"""
	
	bioc = "synapsis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/synapsis_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/synapsis/synapsis_1.8.0.tar.gz"]

	version("1.8.0", sha256="a815a826f739a1c34282e2efb81c539223ea67ad5ee32596f4d8973e73f2c2d0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
