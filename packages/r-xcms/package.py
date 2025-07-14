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

	version("4.6.3", commit="4b1f7c68c1aaf11ed54ff317098e52d78dd3f274")
	version("4.0.2", commit="b27475738be594668e556c5e785b7d9586027e3f")

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
