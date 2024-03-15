# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMzr(RPackage):
	"""parser for netCDF, mzXML, mzData and mzML and mzIdentML files (mass
	spectrometry data).

	mzR provides a unified API to the common file formats and parsers
	available for mass spectrometry data. It comes with a wrapper for the
	ISB random access parser for mass spectrometry mzXML, mzData and mzML
	files. The package contains the original code written by the ISB, and a
	subset of the proteowizard library for mzML and mzIdentML. The netCDF
	reading code has previously been used in XCMS."""

	bioc = "mzR"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mzR_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mzR/mzR_2.36.0.tar.gz"]

	version("2.36.0", md5="aae8b88db5fd49675b653b861702800e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.6:", type=("build", "run"))
	depends_on("r-protgenerics@1.17.3:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rhdf5lib@1.1.4:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
