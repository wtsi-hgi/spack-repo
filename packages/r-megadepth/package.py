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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/megadepth_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/megadepth/megadepth_1.12.0.tar.gz"]

	version("1.12.0", md5="5fa04f9d4075030126388db419378304")

	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-cmdfun", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
