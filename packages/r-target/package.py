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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/target_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/target/target_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="ee135894447e1fd4a1198e1f5dfceb8bd5bafc4f1af4ef9a8df77adc1b3f0a4b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
