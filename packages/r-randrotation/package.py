# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandrotation(RPackage):
	"""Random Rotation Methods for High Dimensional Data with Batch Structure

	A collection of methods for performing random rotations on high-dimensional, normally distributed data (e.g. microarray or RNA-seq data) with batch structure. The random rotation approach allows exact testing of dependent test statistics with linear models following arbitrary batch effect correction methods.
	"""
	
	homepage = "https://github.com/phettegger/randRotation"
	bioc = "randRotation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/randRotation_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/randRotation/randRotation_1.14.0.tar.gz"]

	version("1.14.0", md5="a05faf1fe582450a789fc2d58960fa97")

	depends_on("r-rdpack@0.7:", type=("build", "run"))
