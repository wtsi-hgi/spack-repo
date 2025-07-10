# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
	version("1.48.1", sha256="2af6d1164152f9722fc83cfe16cf43e1a83ba5c9d133d9663175b0ac779e3d51")
	version("1.46.0", commit="80d43e024bead5afd48cb86910ba4670d8d37424")
	version("1.44.0", commit="2e7e0a3b7c1918c0d64170dc7c173a636d3764f4")
	version("1.42.1", commit="d1121696c76c189d6b4df9914806bf585a495845")
	version("1.40.0", commit="50ead7cb60cedf3c053853fab92d9f104f9f85bd")
	version("1.36.0", commit="9918bd19a2e6f89e5edc5fe03c8812f500bb3e19")
	version("1.30.1", commit="fb1ab00872570afb280522c4663e347dafc07a9e")
	version("1.28.13", commit="0393347b8ce2d5edf1a61589be93e6a93eda3419")
	version("1.26.1", commit="60ae67598cc3d7ed20ee6417920f8c209085faaf")
	version("1.24.5", commit="468d7f53fd743e04c9af853d58e871b4cc13a090")
	version("1.22.3", commit="3a91b6d4297aa416d5f056dec6f8925eb1a8eaee")

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
