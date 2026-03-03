# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaldipickr(RPackage):
	"""Dereplicate and Cherry-Pick Mass Spectrometry Spectra

	Convenient wrapper functions for the analysis of
    matrix-assisted laser desorption/ionization-time-of-flight (MALDI-TOF)
    spectra data in order to select only representative spectra (also
    called cherry-pick). The package covers the preprocessing and
    dereplication steps (based on Strejcek, Smrhova, Junkova and Uhlik
    (2018) <doi:10.3389/fmicb.2018.01294>) needed to cluster MALDI-TOF
    spectra before the final cherry-picking step. It enables the easy
    exclusion of spectra and/or clusters to accommodate complex
    cherry-picking strategies. Alternatively, cherry-picking using
    taxonomic identification MALDI-TOF data is made easy with functions to
    import inconsistently formatted reports.
	"""
	
	homepage = "https://github.com/ClavelLab/maldipickr"
	cran = "maldipickr" 

	version("1.3.0", md5="68b74c7a42824a7b2d1cbb150df583a3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maldiquant", type=("build", "run"))
	depends_on("r-readbrukerflexdata", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
