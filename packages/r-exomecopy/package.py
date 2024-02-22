# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExomecopy(RPackage):
	"""Copy number variant detection from exome sequencing read depth.

	Detection of copy number variants (CNV) from exome sequencing samples,
	including unpaired samples. The package implements a hidden Markov model
	which uses positional covariates, such as background read depth and
	GC-content, to simultaneously normalize and segment the samples into
	regions of constant copy count."""

	bioc = "exomeCopy"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/exomeCopy_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/exomeCopy/exomeCopy_1.48.0.tar.gz"]

	version("1.48.0", md5="068f1f0cb675297a1b7940330fae0cbe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges@2.5.27:", type=("build", "run"))
	depends_on("r-genomicranges@1.23.16:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
