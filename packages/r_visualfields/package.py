# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisualfields(RPackage):
	"""Statistical Methods for Visual Fields

	A collection of tools for analyzing the field of vision. It
    provides a framework for development and use of innovative methods for
    visualization, statistical analysis, and clinical interpretation of
    visual-field loss and its change over time. It is intended to be a tool for
    collaborative research. The package is described in Marin-Franch and Swanson
    (2013) <doi:10.1167/13.4.10> and is part of the Open Perimetry Initiative
    (OPI) [Turpin, Artes, and McKendrick (2012) <doi:10.1167/12.11.22>].
	"""
	
	homepage = "https://www.optocom.es"
	cran = "visualFields" 

	version("1.0.1", md5="eff5d25f8185fd4c91f6bab7e591f33e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-oro-dicom", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltable", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
