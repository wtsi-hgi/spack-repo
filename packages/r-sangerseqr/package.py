# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSangerseqr(RPackage):
	"""Tools for Sanger Sequencing Data in R

	This package contains several tools for analyzing Sanger Sequencing data files in R, including reading .scf and .ab1 files, making basecalls and plotting chromatograms.
	"""
	
	bioc = "sangerseqR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sangerseqR_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sangerseqR/sangerseqR_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="234243afead70c7d9b4424b0484c8825ac38a1e24278e53c7ba2d6eafa96efed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
