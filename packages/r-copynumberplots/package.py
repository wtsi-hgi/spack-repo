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

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="1a316f7e53d2e09f2105d4b48886c0c0549eacb2899b927fe1fcada379312cea")

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
