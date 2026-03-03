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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CopyNumberPlots_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CopyNumberPlots/CopyNumberPlots_1.18.0.tar.gz"]

	version("1.18.0", md5="d35c96c521087a1183dd2ae465b3d2a7")

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
