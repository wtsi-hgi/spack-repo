# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopynumberplots(RPackage):
	"""Create Copy-Number Plots using karyoploteR functionality

	CopyNumberPlots have a set of functions extending karyoploteRs functionality to create beautiful, customizable and flexible plots of copy-number related data.
	"""
	
	homepage = "https://github.com/bernatgel/CopyNumberPlots"
	bioc = "CopyNumberPlots"

	version("1.24.0", commit="be5b59c5bafdac5772ae1dee4798ff40d7cab366")
	version("1.18.0", commit="88ca611e759caf58d514ea1d4795edece3b9c94d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-karyoploter", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-cn-mops", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
