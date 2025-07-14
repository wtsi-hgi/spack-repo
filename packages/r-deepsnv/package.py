# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepsnv(RPackage):
	"""Detection of subclonal SNVs in deep sequencing data.

	This package provides provides quantitative variant callers for detecting subclonal mutations in ultra-deep (>=100x coverage) sequencing experiments. The deepSNV algorithm is used for a comparative setup with a control experiment of the same loci and uses a beta-binomial model and a likelihood ratio test to discriminate sequencing errors and subclonal SNVs. The shearwater algorithm computes a Bayes classifier based on a beta-binomial model for variant calling with multiple samples for precisely estimating model parameters - such as local error rates and dispersion - and prior knowledge, e.g. from variation data bases such as COSMIC.
	"""
	
	bioc = "deepSNV" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/deepSNV_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/deepSNV/deepSNV_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="19b9658a182e0b74a994f969a70d790d989ccf67b27535a345bba8953c96b399")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-variantannotation@1.27.6:", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
