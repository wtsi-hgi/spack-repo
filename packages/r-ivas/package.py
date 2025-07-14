# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvas(RPackage):
	"""Identification of genetic Variants affecting Alternative Splicing

	Identification of genetic variants affecting alternative splicing.
	"""
	
	bioc = "IVAS"

	version("2.28.0", commit="aa502bb1f01a7537ff12f8895f167d079a85f69a")
	version("2.22.0", commit="1e105b2074f971452f5de3c85e83c4378a267ed9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
