# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpa(RPackage):
	"""RPA: Robust Probabilistic Averaging for probe-level analysis

	Probabilistic analysis of probe reliability and differential gene expression on short oligonucleotide arrays.
	"""
	
	homepage = "https://github.com/antagomir/RPA"
	bioc = "RPA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RPA_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RPA/RPA_1.58.0.tar.gz"]

	version("1.58.0", md5="ea38f5a76b570c091b8f818c48c836cb")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
