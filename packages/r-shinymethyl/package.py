# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymethyl(RPackage):
	"""Interactive visualization for Illumina methylation arrays

	Interactive tool for visualizing Illumina methylation array data. Both the 450k and EPIC array are supported.
	"""
	
	homepage = "https://github.com/Jfortin1/shinyMethyl"
	bioc = "shinyMethyl" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/shinyMethyl_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/shinyMethyl/shinyMethyl_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="864b844c5a5faf60e970cc63cd099ea0ef3d0598f38dabd76f7af71c700972be")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
