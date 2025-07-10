# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcfarray(RPackage):
	"""Representing on-disk / remote VCF files as array-like objects

	VCFArray extends the DelayedArray to represent VCF data entries as array-like objects with on-disk / remote VCF file as backend. Data entries from VCF files, including info fields, FORMAT fields, and the fixed columns (REF, ALT, QUAL, FILTER) could be converted into VCFArray instances with different dimensions.
	"""
	
	homepage = "https://github.com/Liubuntu/VCFArray"
	bioc = "VCFArray" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VCFArray_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VCFArray/VCFArray_1.18.0.tar.gz"]

	version("1.18.0", sha256="10a87023dd74fe794e8445f4727d230738cdb0df757f9166be73479b32b44d2c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-delayedarray@0.7.28:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-variantannotation@1.29.3:", type=("build", "run"))
	depends_on("r-genomicfiles@1.17.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.19.19:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
