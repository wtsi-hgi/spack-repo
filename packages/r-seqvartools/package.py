# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqvartools(RPackage):
	"""Tools for variant data

	An interface to the fast-access storage format for VCF data provided in SeqArray, with tools for common operations and analysis.
	"""
	
	homepage = "https://github.com/smgogarten/SeqVarTools"
	bioc = "SeqVarTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SeqVarTools_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SeqVarTools/SeqVarTools_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="2b30fe117d2ef1423d0e5177da06ea08004dcdf4459894e10b486aaf5a99c2a5")

	depends_on("r-seqarray", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-gwasexacthw", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
