# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedovariandata(RPackage):
    """Clinically Annotated Data for the Ovarian Cancer Transcriptome

    The curatedOvarianData package provides data for gene expression analysis in patients with ovarian cancer.
    """

    homepage = "http://bcb.dfci.harvard.edu/ovariancancer"
    bioc = "curatedOvarianData"

    version("1.46.2", commit="c01486700ce1b56393ad4ec4fa89e1d8987dc42c")
    version("1.40.1", commit="c16d8042894dbb54e6050b890c6e1c6b8aeac865")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
