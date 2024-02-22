# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnass(RPackage):
	"""Genome-Wide Discovery of Pre-miRNAs with few Labeled Examples

	Machine learning method specifically designed for
    pre-miRNA prediction. It takes advantage of unlabeled sequences to improve
    the prediction rates even when there are just a few positive examples, when
    the negative examples are unreliable or are not good representatives of
    its class. Furthermore, the method can automatically search for negative
    examples if the user is unable to provide them. MiRNAss can find a good
    boundary to divide the pre-miRNAs from other groups of sequences; it
    automatically optimizes the threshold that defines the classes boundaries,
    and thus, it is robust to high class imbalance. Each step of the method is
    scalable and can handle large volumes of data.
	"""
	
	cran = "miRNAss" 

	version("1.5", md5="bd2d819af7ace12a8f4d9d01e76d9bf2")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-corelearn", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
