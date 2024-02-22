# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTarget(RPackage):
	"""Predict Combined Function of Transcription Factors

	Implement the BETA algorithm for infering direct target genes from DNA-binding and perturbation expression data Wang et al. (2013) <doi: 10.1038/nprot.2013.150>. Extend the algorithm to predict the combined function of two DNA-binding elements from comprable binding and expression data.
	"""
	
	homepage = "https://github.com/MahShaaban/target"
	bioc = "target" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/target_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/target/target_1.16.0.tar.gz"]

	version("1.16.0", md5="96ca9fa7bed738941cd930b5e7491bc2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
