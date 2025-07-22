# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("3.32.0", sha256="68a1adac23a4f756bc6369af82f54de57c717bfe1e5e3d54004e3baa01add9c4")
	version("3.30.0", commit="a1882c2126622cb389a7ef1ef5b5c565e603a282")
	version("3.28.0", commit="7749dd7033e9885ec2546a5cac0562bac2fea04d")
	version("3.26.0", commit="7ead7517a77bc8b4b4b42aace69957a17e8fe016")
	version("3.24.0", commit="3ff48b8f546acc9803b3c652363cac78d3b81ae5")
	version("3.20.0", commit="02cde7fa166259bce73c396a87dca2ecc8249c39")
	version("3.16.0", commit="fc16179fc4bee8954c5415d7cd13e3112b75b4fd")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7.1:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
	depends_on("r-matrixstats@0.55:", type=("build", "run"))
