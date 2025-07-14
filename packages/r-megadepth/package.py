# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMegadepth(RPackage):
	"""megadepth: BigWig and BAM related utilities

	This package provides an R interface to Megadepth by Christopher Wilks available at https://github.com/ChristopherWilks/megadepth. It is particularly useful for computing the coverage of a set of genomic regions across bigWig or BAM files. With this package, you can build base-pair coverage matrices for regions or annotations of your choice from BigWig files. Megadepth was used to create the raw files provided by https://bioconductor.org/packages/recount3.
	"""
	
	homepage = "https://github.com/LieberInstitute/megadepth"
	bioc = "megadepth"

	version("1.18.0", commit="f97b3e0a910fb2e278d4b8e01ea3d747e396569b")
	version("1.12.0", commit="13f2d3730c3ecbf80b5455c255b75bb68e0c4ecd")

	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-cmdfun", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
