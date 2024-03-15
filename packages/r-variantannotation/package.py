# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariantannotation(RPackage):
	"""Annotation of Genetic Variants.

	Annotate variants, compute amino acid coding changes, predict coding
	outcomes."""

	bioc = "VariantAnnotation"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VariantAnnotation_1.48.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VariantAnnotation/VariantAnnotation_1.48.1.tar.gz"]

	version("1.48.1", md5="39b6f4907fe37495a903c338e6d4cc73")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.41.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.19.5:", type=("build", "run"))
	depends_on("r-rsamtools@1.99:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-annotationdbi@1.27.9:", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
	depends_on("r-bsgenome@1.47.3:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
	depends_on("r-rhtslib@1.99.3:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
