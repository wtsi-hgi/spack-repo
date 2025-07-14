# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiftover(RPackage):
	"""Changing genomic coordinate systems with rtracklayer::liftOver

	The liftOver facilities developed in conjunction with the UCSC browser track infrastructure are available for transforming data in GRanges formats.  This is illustrated here with an image of the EBI/NHGRI GWAS catalog that is, as of May 10 2017, distributed with coordinates defined by NCBI build hg38.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/liftOver/"
	bioc = "liftOver" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/liftOver_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/liftOver/liftOver_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="c62150ea41127dbbe93df2b6ab0da9aad388198563ae523a1b048dcaeab3d4dd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

