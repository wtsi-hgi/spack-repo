# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecl(RPackage):
	"""specL - Prepare Peptide Spectrum Matches for Use in Targeted Proteomics

	provides a functions for generating spectra libraries that can be used for MRM SRM MS workflows in proteomics. The package provides a BiblioSpec reader, a function which can add the protein information using a FASTA formatted amino acid file, and an export method for using the created library in the Spectronaut software. The package is developed, tested and used at the Functional Genomics Center Zurich <https://fgcz.ch>.
	"""
	
	homepage = "http://bioconductor.org/packages/specL/"
	bioc = "specL" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/specL_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/specL/specL_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="aae46a535b29ae3601c5ef7aafe91167358113dfc256ee22f1a422547ef6a8f9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dbi@0.5:", type=("build", "run"))
	depends_on("r-protviz@0.7:", type=("build", "run"))
	depends_on("r-rsqlite@1.1:", type=("build", "run"))
	depends_on("r-seqinr@3.3:", type=("build", "run"))
