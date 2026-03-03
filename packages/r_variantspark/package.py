# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariantspark(RPackage):
	"""A 'Sparklyr' Extension for 'VariantSpark'

	This is a 'sparklyr' extension integrating 'VariantSpark' and R. 'VariantSpark' is 
  a framework based on 'scala' and 'spark' to analyze genome datasets, 
  see <https://bioinformatics.csiro.au/>. It was tested on datasets with 3000 samples 
  each one containing 80 million features in either unsupervised clustering approaches 
  and supervised applications, like classification and regression. The genome datasets
  are usually writing in VCF, a specific text file format used 
  in bioinformatics for storing gene sequence variations. So, 'VariantSpark' is a great 
  tool for genome research, because it is able to read VCF files, run analyses and return 
  the output in a 'spark' data frame.
	"""
	
	cran = "variantspark" 

	version("0.1.1", md5="53c0b73dd54c3934bcdac74fb3013df6")

	depends_on("r-sparklyr@1.0.1:", type=("build", "run"))
