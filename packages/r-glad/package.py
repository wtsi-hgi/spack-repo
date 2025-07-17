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

    version("2.72.0", commit="3e7d1d18e9eed0e300504d7d19ad5cf751e937e8")
    version("2.66.0", commit="1d3593ce441d35029c0688610a87dbb62789fe38")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-aws", type=("build", "run"))
    depends_on("gsl", type=("build", "link", "run"))

    @run_before("install")
    def set_ac_unique_file(self):
        touch("GLAD")
