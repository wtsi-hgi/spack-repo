# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenspecy(RPackage):
	"""Analyze, Process, Identify, and Share Raman and (FT)IR Spectra

	Raman and (FT)IR spectral analysis tool for plastic particles and
    other environmental samples (Cowger et al. 2021,
    <doi:10.1021/acs.analchem.1c00123>). With read_any(), Open Specy provides a
    single function for reading individual, batch, or map spectral data files
    like .asp, .csv, .jdx, .spc, .spa, .0, and .zip. process_spec() simplifies
    processing spectra, including smoothing, baseline correction,
    range restriction and flattening, intensity conversions, wavenumber
    alignment, and min-max normalization. Spectra can be identified in batch
    using an onboard reference library (Cowger et al. 2020,
    <doi:10.1177/0003702820929064>) using match_spec(). A Shiny app is available
    via run_app() or online at <https://openanalysis.org/openspecy/>.
	"""
	
	homepage = "https://github.com/wincowgerDEV/OpenSpecy-package/"
	cran = "OpenSpecy" 

	version("1.0.8", md5="2336c2c5405d2b7344b7425f32eda5ae")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-osfr", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-hyperspec", type=("build", "run"))
	depends_on("r-mmand", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
