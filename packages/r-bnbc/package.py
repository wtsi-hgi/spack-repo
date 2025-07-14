# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnbc(RPackage):
	"""Bandwise normalization and batch correction of Hi-C data

	Tools to normalize (several) Hi-C data from replicates.
	"""
	
	homepage = "https://github.com/hansenlab/bnbc"
	bioc = "bnbc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bnbc_1.24.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bnbc/bnbc_1.24.2.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.2", sha256="fb19ad8721cb36a57d5bf7949c12d309a5ebc314ada4b95fd2abf833f650683b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-hicbricks", type=("build", "run"))
