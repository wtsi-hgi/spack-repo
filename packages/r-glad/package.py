# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlad(RPackage):
    """Gain and Loss Analysis of DNA

    Analysis of array CGH data : detection of breakpoints in genomic profiles and assignment of a status (gain, normal or loss) to each chromosomal regions identified.
    """

    homepage = "http://bioinfo.curie.fr"
    bioc = "GLAD"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GLAD_2.66.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GLAD/GLAD_2.66.0.tar.gz",
    ]

    version("2.66.0", sha256="a14c769b423fb99d744d95948f33b7e8ed0dd23d40e25188d2e767668afd9e13")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-aws", type=("build", "run"))
    depends_on("gsl", type=("build", "link", "run"))

    @run_before("install")
    def set_ac_unique_file(self):
        touch("GLAD")
