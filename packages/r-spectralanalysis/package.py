# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralanalysis(RPackage):
	"""Pre-Process, Visualize and Analyse Spectral Data

	
    Infrared, near-infrared and Raman spectroscopic data measured during chemical reactions, provide structural fingerprints by which molecules can be identified and quantified. The application of these spectroscopic techniques as inline process analytical tools (PAT), provides the pharmaceutical and chemical industry with novel tools, allowing to monitor their chemical processes, resulting in a better process understanding through insight in reaction rates, mechanistics, stability, etc.
    Data can be read into R via the generic spc-format, which is generally supported by spectrometer vendor software. Versatile pre-processing functions are available to perform baseline correction by linking to the 'baseline' package; noise reduction via the 'signal' package; as well as time alignment, normalization, differentiation, integration and interpolation. Implementation based on the S4 object system allows storing a pre-processing pipeline as part of a spectral data object, and easily transferring it to other datasets. Interactive plotting tools are provided based on the 'plotly' package. 
    Non-negative matrix factorization (NMF) has been implemented to perform multivariate analyses on individual spectral datasets or on multiple datasets at once. NMF provides a parts-based representation of the spectral data in terms of spectral signatures of the chemical compounds and their relative proportions.
    See 'hNMF'-package for references on available methods. The functionality to read in spc-files was adapted from the 'hyperSpec' package.
	"""
	
	homepage = "https://openanalytics.eu"
	cran = "spectralAnalysis" 

	version("4.3.3", md5="8c81d71101dccfa66c2882772fc5b061")

	depends_on("r-baseline", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-hnmf", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
