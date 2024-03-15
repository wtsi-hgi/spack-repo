# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAromaLight(RPackage):
	"""Light-Weight Methods for Normalization and Visualization of Microarray
	Data using Only Basic R Data Types.

	Methods for microarray analysis that take basic data types such as
	matrices and lists of vectors. These methods can be used standalone, be
	utilized in other packages, or be wrapped up in higher-level classes."""

	bioc = "aroma.light"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/aroma.light_3.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/aroma.light/aroma.light_3.32.0.tar.gz"]

	version("3.32.0", md5="07d98bcf8be950a16c1d6aaae375f17d")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7.1:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
	depends_on("r-matrixstats@0.55:", type=("build", "run"))
