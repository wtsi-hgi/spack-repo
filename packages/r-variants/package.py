# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariants(RPackage):
	"""Annotating Genomic Variants

	Read and write VCF files. Identify structural location of variants and compute amino acid coding changes for non-synonymous variants. Use SIFT and PolyPhen database packages to predict consequence of amino acid coding changes.
	"""
	
	homepage = "https://bioconductor.org/help/workflows/variants/"
	bioc = "variants" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/variants_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/variants/variants_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="1146bdda61d1de000cfad7d22edb035da9520a8d28bc4afc1a0e3f6c0584adc5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-polyphen-hsapiens-dbsnp131", type=("build", "run"))

