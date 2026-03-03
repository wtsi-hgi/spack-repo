# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamanmp(RPackage):
	"""Analysis and Identification of Raman Spectra of Microplastics

	Pre-processing and polymer identification of Raman spectra of plastics. Pre-processing includes normalisation functions, peak identification based on local maxima, smoothing process and removal of spectral region of no interest. Polymer identification can be performed using Pearson correlation coefficient or Euclidean distance (Renner et al. (2019), <doi:10.1016/j.trac.2018.12.004>), and the comparison can be done with a user-defined database or with the database already implemented in the package, which currently includes 356 spectra, with several spectra of plastic colorants.
	"""
	
	cran = "RamanMP" 

	version("1.0", md5="97085a8a11e1217c9a741e6aaac7d42d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
