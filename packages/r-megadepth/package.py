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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/megadepth_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/megadepth/megadepth_1.12.0.tar.gz"]

	version("1.12.0", sha256="83ed546eb617661c69ea8928acfe5f72b9c9085b0fbb12140dda0bb80d262d3d")

	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-cmdfun", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
