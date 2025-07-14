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

	version("1.8.0", commit="7d5156694a726b174f3d15aa1f7ab27e52185a87")
	version("1.2.0", commit="1a436b8dcaa1301c1dd368b43aec7c49bfdf322b")

	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
	depends_on("r-alabaster-string", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
