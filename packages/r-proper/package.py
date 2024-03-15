# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProper(RPackage):
	"""PROspective Power Evaluation for RNAseq

	This package provide simulation based methods for evaluating the statistical power in differential expression analysis from RNA-seq data.
	"""
	
	bioc = "PROPER" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PROPER_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PROPER/PROPER_1.34.0.tar.gz"]

	version("1.34.0", md5="6f91ce4b3f5feee476a991fc1072c521")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
