# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstherm(RPackage):
	"""Analyze MS/MS Protein Melting Data

	Software to aid in modeling and analyzing mass-spectrometry-based
    proteome melting data. Quantitative data is imported and normalized and
    thermal behavior is modeled at the protein level. Methods exist for
    normalization, modeling, visualization, and export of results. For a
    general introduction to MS-based thermal profiling, see Savitski et al.
    (2014) <doi:10.1126/science.1255784>.
	"""
	
	cran = "mstherm" 

	version("0.4.7", md5="600a6ec96f8a2c92fbfa8f52fe359cf9")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
