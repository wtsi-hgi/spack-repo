# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXcms(RPackage):
	"""LC-MS and GC-MS Data Analysis

	Framework for processing and visualization of chromatographically separated and single-spectra mass spectral data. Imports from AIA/ANDI NetCDF, mzXML, mzData and mzML files. Preprocesses data for high-throughput, untargeted analyte profiling.
	"""
	
	homepage = "https://github.com/sneumann/xcms"
	bioc = "xcms" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/xcms_4.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/xcms/xcms_4.0.2.tar.gz"]

	version("4.0.2", md5="8649eeacc3e82397f8d6c700e4d34834")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocparallel@1.8:", type=("build", "run"))
	depends_on("r-msnbase@2.23.1:", type=("build", "run"))
	depends_on("r-mzr@2.25.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-protgenerics@1.29.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-massspecwavelet@1.66:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-mscoreutils@1.11.5:", type=("build", "run"))
	depends_on("r-msfeatures", type=("build", "run"))
	depends_on("r-msexperiment@1.1.2:", type=("build", "run"))
	depends_on("r-spectra@1.11.10:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
