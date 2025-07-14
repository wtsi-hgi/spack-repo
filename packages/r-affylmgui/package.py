# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffylmgui(RPackage):
	"""GUI for limma Package with Affymetrix Microarrays

	A Graphical User Interface (GUI) for analysis of Affymetrix microarray gene expression data using the affy and limma packages.
	"""
	
	homepage = "http://bioinf.wehi.edu.au/affylmGUI/"
	bioc = "affylmGUI"

	version("1.82.0", commit="1da3343fef0ed3956b95a9cb8573758e1698bf88")
	version("1.76.0", commit="d6a5c351689e52e6633a89fd34a31297a169b45d")

	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyio", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
