# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5lib(RPackage):
	"""hdf5 library as an R package.

	Provides C and C++ hdf5 libraries."""

	bioc = "Rhdf5lib"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rhdf5lib_1.24.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rhdf5lib/Rhdf5lib_1.24.2.tar.gz"]
	version("1.6.3", commit="11ac3069f28b0068002db9c645817401f6c5b3c4")
	version("1.4.3", commit="f6be8c2659b2daa17541506058917b7981490d65")
	version("1.24.2", md5="d350d5309740f184ad4eec7cdb6d705b")
	version("1.22.0", commit="2bf06b364e8d478549b07a298eaf60177a050dc9")
	version("1.20.0", commit="760679995f17996a9de328cf7a8bcaa6c87286d4")
	version("1.2.1", commit="dbf85dbedb736d5a696794d52875729c8514494e")
	version("1.18.2", commit="d104bbfdb91ac5ec7db3c453f23e4d1d6feb671f")
	version("1.16.0", commit="534c49705dbdb27ae0c564acff2c72df2b27b3f1")
	version("1.12.1", commit="cf464f40fd95274d0d351cf28b586c49307c4f0b")
	version("1.0.0", commit="79608038c2016a518ba747fe6a2bf02ce53a75f9")

	depends_on("r@4.2:", type=("build", "run"), when="@1.22:")
	depends_on("zlib", type=("build", "link", "run"))
