# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafh5GnomadV312Grch38(RPackage):
	"""Minor allele frequency data from gnomAD version 3.1.2 for GRCh38

	Store minor allele frequency data from the Genome Aggregation Database (gnomAD version 3.1.2) for the human genome version GRCh38.
	"""
	
	bioc = "MafH5.gnomAD.v3.1.2.GRCh38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafH5.gnomAD.v3.1.2.GRCh38_3.15.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MafH5.gnomAD.v3.1.2.GRCh38/MafH5.gnomAD.v3.1.2.GRCh38_3.15.0.tar.gz"]

	version("3.15.0", md5="e9c85173866caf998cf1af7dd35aac0b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafH5.gnomAD.v3.1.2.GRCh38_3.15.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicscores@2.7.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))

