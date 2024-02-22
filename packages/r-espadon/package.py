# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REspadon(RPackage):
	"""Easy Study of Patient DICOM Data in Oncology

	Exploitation, processing and 2D-3D visualization of DICOM-RT files (structures, dosimetry, imagery) for medical physics and clinical research, in a patient-oriented perspective.
	"""
	
	homepage = "https://espadon.cnrs.fr"
	cran = "espadon" 

	version("1.5.1", md5="6c16c08af57e2d4c87e4b4cc4f20ede4")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-js", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rgl@1.1.3:", type=("build", "run"))
	depends_on("r-rvcg@0.22.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
