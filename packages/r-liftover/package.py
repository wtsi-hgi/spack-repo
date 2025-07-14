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

	version("1.32.0", commit="70337fff5ba1ae1df05f1e7221bba64bf00cf539")
	version("1.26.0", commit="9f987c73a66c70c81185c9db1d12dd7dd54d1aed")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

