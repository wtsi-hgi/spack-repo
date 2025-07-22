# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabocoreutils(RPackage):
    """Core Utils for Metabolomics Data

    MetaboCoreUtils defines metabolomics-related core functionality provided as low-level functions to allow a data structure-independent usage across various R packages. This includes functions to calculate between ion (adduct) and compound mass-to-charge ratios and masses or functions to work with chemical formulas. The package provides also a set of adduct definitions and information on some commercially available internal standard mixes commonly used in MS experiments.
    """

    homepage = "https://github.com/RforMassSpectrometry/MetaboCoreUtils"
    bioc = "MetaboCoreUtils"

    version("1.16.1", commit="4c476925497886ed1b44e0bd250be71c1deb972a")
    version("1.10.0", commit="4c181cc74f8e456551ef74debcc25bbb6095d23d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
