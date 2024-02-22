# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpaexample(RPackage):
	"""Example data for the GPA package (Genetic analysis incorporating Pleiotropy and Annotation)

	Example data for the GPA package, consisting of the p-values of 1,219,805 SNPs for five psychiatric disorder GWAS from the psychiatric GWAS consortium (PGC), with the annotation data using genes preferentially expressed in the central nervous system (CNS).
	"""
	
	homepage = "http://dongjunchung.github.io/GPA/"
	bioc = "gpaExample" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/gpaExample_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/gpaExample/gpaExample_1.14.0.tar.gz"]

	version("1.14.0", md5="e989af58ed5bbc10573f7438b3ee7836")

	depends_on("r@4:", type=("build", "run"))

	# experiment