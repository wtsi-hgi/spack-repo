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

	version("1.20.0", commit="bf1e5acf04dd7cbe22b87ba0e14cd859e772e79b")
	version("1.14.0", commit="1379847fa94bb7af84f1b336a4f147494ddb62b9")

	depends_on("r@4:", type=("build", "run"))

