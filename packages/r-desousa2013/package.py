# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesousa2013(RPackage):
	"""Poor prognosis colon cancer is defined by a molecularly distinct subtype and precursor lesion

	This package reproduces the main pipeline to analyze the AMC-AJCCII-90 microarray data set in De Sousa et al. accepted by Nature Medicine in 2013.
	"""
	
	bioc = "DeSousa2013"

	version("1.44.0", commit="bbc47d28f8e76eb652303b4df2b189cee761ed80")
	version("1.38.0", commit="ee32611263d0aaf3f59dfd0185a8c7ae68100a54")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-frma", type=("build", "run"))
	depends_on("r-frmatools", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))
	depends_on("r-hgu133plus2frmavecs", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

