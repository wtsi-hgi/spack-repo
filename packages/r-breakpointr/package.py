# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakpointr(RPackage):
	"""Find breakpoints in Strand-seq data

	This package implements functions for finding breakpoints, plotting and export of Strand-seq data.
	"""
	
	homepage = "https://github.com/daewoooo/BreakPointR"
	bioc = "breakpointR"

	version("1.26.0", commit="5c9bee3f3afed79a02c5ea38e30621ecb80bce58")
	version("1.20.0", commit="eef3f27918325baa40470be0a481e49835fd1469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-breakpointrdata", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb@1.12.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
