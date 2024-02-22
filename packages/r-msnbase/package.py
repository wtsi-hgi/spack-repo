# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsnbase(RPackage):
	"""Base Functions and Classes for Mass Spectrometry and Proteomics.

	MSnbase provides infrastructure for manipulation, processing and
	visualisation of mass spectrometry and proteomics data, ranging from raw
	to quantitative and annotated data."""

	bioc = "MSnbase"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSnbase_2.28.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSnbase/MSnbase_2.28.1.tar.gz"]

	version("2.28.1", md5="4d3cbd696e9ca193ec9bdc4722f2ac49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.7.1:", type=("build", "run"))
	depends_on("r-biobase@2.15.2:", type=("build", "run"))
	depends_on("r-mzr@2.29.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-protgenerics@1.29.1:", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges@2.13.28:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-maldiquant@1.16:", type=("build", "run"))
	depends_on("r-mzid@1.5.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
