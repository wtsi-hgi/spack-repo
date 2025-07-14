# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsa2dist(RPackage):
	"""MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis

	MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis. It uses scoring matrices to be used in these pairwise distance calcualtions which can be adapted to any scoring for DNA or AA characters. E.g. by using literal distances MSA2dist calculates pairwise IUPAC distances.
	"""
	
	homepage = "https://gitlab.gwdg.de/mpievolbio-it/MSA2dist"
	bioc = "MSA2dist" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSA2dist_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSA2dist/MSA2dist_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="3a2cb8cfd1af85866df1ff9b8d8f33a0b691600353e5201853a9b3956e362df8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
