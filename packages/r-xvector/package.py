# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXvector(RPackage):
	"""Foundation of external vector representation and manipulation in
	Bioconductor.

	Provides memory efficient S4 classes for storing sequences "externally"
	(e.g. behind an R external pointer, or on disk)."""

	bioc = "XVector"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/XVector_0.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/XVector/XVector_0.42.0.tar.gz"]
	version("0.40.0", commit="875b4b4469e125737bee42362e7a3c75edd642f1")
	version("0.38.0", commit="8cad08446091dcc7cd759e880c0f3e47228278dd")
	version("0.36.0", commit="ff6f818ff4357eb9bf00654de9e0f508a5285408")
	version("0.34.0", commit="06adb25ac51c707b90fb8e0637fa06df237a863c")
	version("0.30.0", commit="985e963e0b1c3ff004dd0b07ad7c9ff7ed853ec0")
	version("0.24.0", commit="e5109cb2687724b9fddddf296c07a82bae4c551d")
	version("0.22.0", commit="b5e107a5fd719e18374eb836eb498b529afa4473")
	version("0.20.0", commit="a83a7ea01f6a710f0ba7d9fb021cfa795b291cb4")
	version("0.18.0", commit="27acf47282c9880b54d04dff46c1e50f0c87fa6b")
	version("0.16.0", commit="54615888e1a559da4a81de33e934fc0f1c3ad99f")
	version("0.42.0", md5="f126998c6b563132e51ea31c3995c6b9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
