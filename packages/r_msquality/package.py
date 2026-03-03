# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsquality(RPackage):
	"""MsQuality - Quality metric calculation from Spectra and MsExperiment objects

	The MsQuality provides functionality to calculate quality metrics for mass spectrometry-derived, spectral data at the per-sample level. MsQuality relies on the mzQC framework of quality metrics defined by the Human Proteom Organization-Proteomics Standards Initiative (HUPO-PSI). These metrics quantify the quality of spectral raw files using a controlled vocabulary. The package is especially addressed towards users that acquire mass spectrometry data on a large scale (e.g. data sets from clinical settings consisting of several thousands of samples). The MsQuality package allows to calculate low-level quality metrics that require minimum information on mass spectrometry data: retention time, m/z values, and associated intensities. MsQuality relies on the Spectra package, or alternatively the MsExperiment package, and its infrastructure to store spectral data.
	"""
	
	homepage = "https://www.github.com/tnaake/MsQuality/"
	bioc = "MsQuality" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsQuality_1.2.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsQuality/MsQuality_1.2.1.tar.gz"]

	version("1.2.1", md5="8eeb5c16239c807ddddd36ae1b5026fa")
	version("1.2.0", md5="1d8e2101f472e8fc93bfa275db511982")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel@1.32:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-msdata@0.32:", type=("build", "run"))
	depends_on("r-msexperiment@0.99:", type=("build", "run"))
	depends_on("r-plotly@4.9.4.1:", type=("build", "run"))
	depends_on("r-protgenerics@1.24:", type=("build", "run"))
	depends_on("r-rmzqc@0.5:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.1:", type=("build", "run"))
	depends_on("r-spectra@1.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
