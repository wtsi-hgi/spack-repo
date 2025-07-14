# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrderedlist(RPackage):
	"""Similarities of Ordered Gene Lists

	Detection of similarities between ordered lists of genes. Thereby, either simple lists can be compared or gene expression data can be used to deduce the lists. Significance of similarities is evaluated by shuffling lists or by resampling in microarray data, respectively.
	"""
	
	homepage = "http://compdiag.molgen.mpg.de/software/OrderedList.shtml"
	bioc = "OrderedList" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OrderedList_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OrderedList/OrderedList_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="ea42c6eb35123196f913938f10e2ccdbf56caaafa4738a536391af0dee3ae25e")

	depends_on("r@3.6.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-twilight", type=("build", "run"))
