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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/gpaExample_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/gpaExample/gpaExample_1.14.0.tar.gz"]

	version("1.14.0", sha256="0995e0892f028ffee5ed68f897f4bbb973db55d3c7b12b0c4a9b629978775635")

	depends_on("r@4:", type=("build", "run"))

