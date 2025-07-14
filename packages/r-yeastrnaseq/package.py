# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastrnaseq(RPackage):
	"""Yeast RNA-Seq Experimental Data from Lee et al. 2008

	A selection of RNA-Seq data from a yeast transcriptome experiment.
	"""
	
	bioc = "yeastRNASeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/yeastRNASeq_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/yeastRNASeq/yeastRNASeq_0.40.0.tar.gz"]

    version("0.46.0", tag="RELEASE_3_21")
	version("0.40.0", sha256="f56ab47df663d826fb57003bae2f47740cd23a3e2bb54a2e269d1af8fd6aebac")

	depends_on("r@2.4:", type=("build", "run"))

