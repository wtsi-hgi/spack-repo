# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoutroslabPlottingGeneral(RPackage):
	"""Functions to Create Publication-Quality Plots

	Contains several plotting functions such as barplots, scatterplots, heatmaps, as well as functions to combine plots and assist in the creation of these plots. These functions will give users great ease of use and customization options in broad use for biomedical applications, as well as general purpose plotting. Each of the functions also provides valid default settings to make plotting data more efficient and producing high quality plots with standard colour schemes simpler. All functions within this package are capable of producing plots that are of the quality to be presented in scientific publications and journals. P'ng et al.; BPG: Seamless, automated and interactive visualization of scientific data; BMC Bioinformatics 2019 <doi:10.1186/s12859-019-2610-2>.
	"""
	
	homepage = "https://github.com/uclahs-cds/package-BoutrosLab-plotting-general"
	cran = "BoutrosLab.plotting.general" 

	version("7.1.0", md5="8a14d03937fb6a9c4da9e000a019bb3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice@0.20.35:", type=("build", "run"))
	depends_on("r-latticeextra@0.6.27:", type=("build", "run"))
	depends_on("r-cluster@2:", type=("build", "run"))
	depends_on("r-hexbin@1.27:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass@7.3.29:", type=("build", "run"))
