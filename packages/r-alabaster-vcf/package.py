# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterVcf(RPackage):
	"""Save and Load Variant Data to/from File

	Save variant calling SummarizedExperiment to file and load them back as VCF objects. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.vcf" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster.vcf_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster.vcf/alabaster.vcf_1.2.0.tar.gz"]

	version("1.2.0", sha256="29326985006669d777daaf9e2134149754a9e99cb6f2f0d0afe32e118265fc77")

	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
	depends_on("r-alabaster-string", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
