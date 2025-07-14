# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyilm(RPackage):
	"""Linear Model of background subtraction and the Langmuir isotherm.

	affyILM is a preprocessing tool which estimates gene expression levels
	for Affymetrix Gene Chips. Input from physical chemistry is employed to
	first background subtract intensities before calculating concentrations
	on behalf of the Langmuir model."""

	bioc = "affyILM"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/affyILM_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/affyILM/affyILM_1.54.0.tar.gz"]

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="5b9fbf8552b47d24f4814c607837e5e9185d7506684350a1bc96ed77d0616fe9")
	version("1.52.0", commit="08ed8c60921ba1b9e04fa90e156eef1a3c899d15")
	version("1.50.0", commit="185cd8e4712a3378ce7a156d4940224bbb2c4122")
	version("1.48.0", commit="4603a4c4d6c2330a8a56a7bb657dc56c51a9393a")
	version("1.46.0", commit="67ffbfa6c881ed83d15604bf4463fe5dba81036b")
	version("1.42.0", commit="b97b29786b866de38802ebbb995169be91e90942")
	version("1.36.0", commit="619ced931ba72860ce4cb41c841bbca1636a1132")
	version("1.34.0", commit="2c02ed2d8fa9a9585d41cf4db0b75d0a07ad8564")
	version("1.32.0", commit="860f2ddada80435d309ba334eff3fab503817755")
	version("1.30.0", commit="c07d91ae52a2a48f0a5f212c3ecf3243741bee13")
	version("1.28.0", commit="307bee3ebc599e0ea4a1d6fa8d5511ccf8bef7de")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-affxparser@1.16:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
