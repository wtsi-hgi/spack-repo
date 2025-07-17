# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHem(RPackage):
    """Heterogeneous error model for identification of differentially expressed genes under multiple conditions

    This package fits heterogeneous error models for analysis of microarray data
    """

    homepage = (
        "http://www.healthsystem.virginia.edu/internet/hes/biostat/bioinformatics/"
    )
    bioc = "HEM"

    version("1.80.0", commit="0c872b23bbe3423ffdde54fd2fdfc1dea36525dc")
    version("1.74.0", commit="dba767f812504381eafd5c129425436a4a377bd2")

    depends_on("r@2.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
